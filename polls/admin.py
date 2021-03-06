import os

from django.contrib import admin
from django.db import models
from django.conf.urls import url
from django.urls import path
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string

# Register your models here.

from .models import Positions,Candidate,Bucket,TokenDash,ConfigVars,Voters
import polls.bucket as bucket
# from .models import Positions,Candidate,Bucket,ConfigVars
from . import views
from polls.auth import getUnusedTokens, genPassword
from polls.vote import tallyAllVotes
import polls.util as util
import polls.globals as globals

admin.site.site_header = "eVoting Admin"
admin.site.site_title = "eVoting Admin Portal"
admin.site.index_title = "Welcome to eVoting Portal"
admin.site.register(Positions)
admin.site.register(Bucket)
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    readonly_fields = ['votes']

@admin.register(Voters)
class VotersAdmin(admin.ModelAdmin):
    readonly_fields = ['hasVoted']

# @todo: permission level
@admin.register(TokenDash)
class TokenDashAdmin(admin.ModelAdmin):
    change_list_template = 'admin/token_dash.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        tokens = []
        try:
            tokens = getUnusedTokens()
        except (AttributeError, KeyError):
            return response
        response.context_data['tokens'] = tokens
        response.context_data['noOfTokens'] = len(tokens)
        
        return response


@admin.register(ConfigVars)
class ConfigVarsAdmin(admin.ModelAdmin):
    change_list_template = "admin/action_buttons.html"
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('start/', self.startPoll),
            path('stop/', self.stopPoll),
            path('publishResults/', self.publishResults),
            path('unpublish/', self.unpublish),
            path('fileUpload/', self.fileUpload),
            path('addVoter/', self.addVoter),
            path('sendCredentialsEmail/', self.sendCredentialsEmail),
            path('sendSingleCredentialsEmail/', self.sendSingleCredentialsEmail),
        ]
        return my_urls + urls
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        util.initConfigTable()
        results = []
        try:
            results = bucket.fetchPositions(None)
        except (AttributeError, KeyError):
            return response
        ongoingVal = self.model.objects.get(varKey='ongoing').varVal
        publishedVal = self.model.objects.get(varKey='publish').varVal
        response.context_data['status'] = "The poll is currently {}. Results of the poll are {}.".format(
            "in process" if ongoingVal == 1 else "not running", "not yet published" if publishedVal == 0 else "published on the homepage.")
        response.context_data['positions'] = results
        response.context_data['published'] = publishedVal
        
        return response
        
    def startPoll(self, request): # @todo: programatically add these config vars on migrate
        self.model.objects.filter(varKey='ongoing').update(varVal=1)
        self.message_user(request, "Started poll.")
        return HttpResponseRedirect("../")

    def stopPoll(self, request):
        self.model.objects.filter(varKey='ongoing').update(varVal=0)
        self.message_user(request, "Stopped poll.")
        return HttpResponseRedirect("../")

    def publishResults(self, request):
        self.model.objects.filter(varKey='publish').update(varVal=1)
        self.tally = tallyAllVotes(verify_votes=True, commit_tally=True)
        self.message_user(request, "Calculated results and published on home page.")
        return HttpResponseRedirect("../")

    def unpublish(self, request):
        self.model.objects.filter(varKey='publish').update(varVal=0)
        self.tally = tallyAllVotes(verify_votes=True, commit_tally=True)
        self.message_user(request, "Calculated results and published on home page.")
        return HttpResponseRedirect("../")
    
    def fileUpload(self, request):
        upload_dir = 'uploads/'
        noOfEntries = 0
        if request.FILES['users'] and request.POST.get('roll','') != '' and request.POST.get('webmail','') != '':
            myfile = request.FILES['users']
            fs = FileSystemStorage(location=upload_dir)
            filename = fs.save(myfile.name, myfile)
            # add parsed table data here
            upload_path = os.path.join(fs.location, filename)
            result = util.parseEmailIds(upload_path, request.POST.get('roll',''), request.POST.get('webmail',''))
            if result['status'] == False:
                self.message_user(request, result['data'])
                return HttpResponseRedirect("../")
            else:
                roll_no_li = result['data'][0]
                webmail_li = result['data'][1]
                voters = []
                existing_voterIDs = list(Voters.objects.values_list('voterID', flat=True))
                for roll_no, webmail in zip(roll_no_li, webmail_li):
                    if roll_no not in existing_voterIDs:
                        voters.append(Voters(voterID=roll_no, webmail=webmail))
                    else:
                        v = Voters(voterID=roll_no, webmail=webmail)
                        v.save()
                        noOfEntries += 1
                noOfEntries += len(voters)
                Voters.objects.bulk_create(voters)

        self.message_user(request, "Data parsed for {} entries and file uploaded at: {}".format(noOfEntries, upload_path))
        return HttpResponseRedirect("../")

    def addVoter(self, request):
        if request.POST.get('rollNo','') != '' and request.POST.get('webmail','') != '':
            voter = Voters(voterID=request.POST.get('rollNo',''))
            voter.webmail = request.POST.get('webmail','')
            voter.save()
        self.message_user(request, "Voter added : {}".format(request.POST.get('rollNo','')))
        return HttpResponseRedirect("../")

    def sendCredentialsEmail(self, request):
        noOfEmails = 0
        voterData = Voters.objects.all()
        for voter in voterData: 
            pswd = genPassword(voter.voterID)
            htmlData = ""
            templateData = globals.globals.copy()
            templateData.update({ 'password' : pswd })
            htmlData = render_to_string('email/credential.html', templateData) 
            util.sendMail(
                voter.webmail or '' ,
                "Credentials for voting portal.",
                globals.emailTemplates['credential'].format(pswd),
                htmlData
            )
            noOfEmails += 1
        # self.model.objects.filter(varKey='publish').update(varVal=0)
        self.message_user(request, "Emails with credentials sent to {} webmail IDs.".format(noOfEmails))
        return HttpResponseRedirect("../")
    

    def sendSingleCredentialsEmail(self, request):
        if request.POST.get('roll','') != '' and request.POST.get('webmail','') != '':
            try:
                voterData = Voters.objects.get(voterID=request.POST.get('roll',''))
                voterData.webmail = request.POST.get('webmail','')
                voterData.save()
                pswd = genPassword(voterData.voterID)
                htmlData = ""
                templateData = globals.globals.copy()
                templateData.update({ 'password' : pswd })
                htmlData = render_to_string('email/credential.html', templateData) 
                util.sendMail(
                    voterData.webmail or '' ,
                    "Credentials for voting portal.",
                    globals.emailTemplates['credential'].format(pswd),
                    htmlData
                )
                self.message_user(request, "Email sent")
            except Voters.DoesNotExist:
                self.message_user(request, "Roll No. not found.")    
        else:
            self.message_user(request, "Email not sent : Invalid RollNo or Webmail ID")    
        # self.model.objects.filter(varKey='publish').update(varVal=0)
        return HttpResponseRedirect("../")
