from django.contrib import admin
from django.db import models
from django.conf.urls import url

# Register your models here.

from .models import Positions,Candidate,Bucket,TokenDash,TokenNo
from . import views

admin.site.register(Positions)
admin.site.register(Bucket)
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    readonly_fields = ['votes']
    # exclude = ('votes',)

# @todo: permission level
@admin.register(TokenDash)
class TokenDashAdmin(admin.ModelAdmin):
    change_list_template = 'admin/token_dash.html'
    add_url = ''
    # date_hierarchy = 'created'
    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(
    #         request,
    #         extra_context=extra_context,
    #     )
    #     try:
    #         query = TokenNo.objects.filter()
    #     except (AttributeError, KeyError):
    #         return response
    #     response.context_data['summary'] = list(
    #         qs
    #         .values('sale__category__name')
    #         .annotate(**metrics)
    #         .order_by('-total_sales')
    #     )
        
    #     return response

