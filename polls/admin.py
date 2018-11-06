from django.contrib import admin
from django.db import models
from django.conf.urls import url
from django.urls import path
from django.http import HttpResponse,HttpResponseRedirect

# Register your models here.

from .models import Positions,Candidate,Bucket,TokenDash,ConfigVars
import polls.bucket as bucket
# from .models import Positions,Candidate,Bucket,ConfigVars
from . import views
from polls.auth import getUnusedTokens
from polls.vote import tallyAllVotes
import polls.util as util
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
