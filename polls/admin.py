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
            path('sendCredentialsEmail/', self.sendCredentialsEmail),
            path('addVoter/', self.addVoter),
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
        noOfEntries = 0
        if request.FILES['users'] and request.POST.get('roll','') != '' and request.POST.get('webmail','') != '':
            myfile = request.FILES['users']
            fs = FileSystemStorage(location='uploads/')
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            # add parsed table data here.
            # voter = Voters(voterID=voterID).save()
        # self.model.objects.filter(varKey='publish').update(varVal=0)
        self.message_user(request, "Data parsed for {} entries and file uploaded at: {}".format(noOfEntries, uploaded_file_url))
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
