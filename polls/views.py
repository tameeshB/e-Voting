from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('polls/index.html')
    context = {
        'electionName' : 'Gymkhana Elections 2018',
        'hasBegun' : True,
        'hoursUntilEnd' : 10,
        'user': 'tameeshb',
        'positions' : [
            {
                'posName':'VP',
                'posID' : 'vp',
                'candidates':[
                    {'voterID':'1601CS20','name':'Parth Kulkarni','agendaURL':'https://facebook.com'},
                    {'voterID':'1601CS21','name':'Manish Kumar','agendaURL':'https://facebook.com'},
                    {'voterID':'1601CS22','name':'Mayank Vaidya','agendaURL':'https://facebook.com'}
                ]
            },
            {
                'posName':'TechSec',
                'posID' : 'techsec',
                'candidates':[
                    {'voterID':'1601CS20','name':'Parth Kulkarni','agendaURL':'https://facebook.com'},
                    {'voterID':'1601CS21','name':'Manish Kumar','agendaURL':'https://facebook.com'},
                    {'voterID':'1601CS22','name':'Mayank Vaidya','agendaURL':'https://facebook.com'}
                ]
            }
        ]
    }
    return HttpResponse(template.render(context, request))