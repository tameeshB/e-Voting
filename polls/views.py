from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.contrib import messages

import polls.auth as auth
import polls.util as util
import polls.globals as globals
import polls.bucket as bucket

# Create your views here.
def index(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(globals.globals, request))

def login(request):
    print(request.POST)
    messageList = []
    # print(type(request.POST['name']))
    if request.POST:
        try:
            authResult =  auth.authenticate(request.POST['name'],request.POST['password'],request.POST['token'])
            if authResult == True:
                request.session['token'] = request.POST['token']
                request.session['rollno'] = request.POST['name']
                request.session['bucket'] = bucket.process(request.POST['name'],request.session['hostel'],request.session['gender'])
                print('Authenticated!')
                return HttpResponseRedirect(reverse('polls:vote'))
            else:
                messageList.append(authResult)
        except KeyError:
            pass
        except MultiValueDictKeyError:
            pass
    
    context = {}
    context.update(globals.globals)
    messageList.extend(messages.get_messages(request))
    context.update({'messages': messageList})
    
    return render(request, 'polls/index.html', context)

def vote(request):
    # Not authenticated
    if 'token' not in request.session.keys():
        messages.add_message(request, messages.ERROR, 'Please log-in before voting.')
        return HttpResponseRedirect(reverse('polls:login'))
    positions = bucket.fetchPositions(request.session['bucket'])
    context = {}
    context.update(globals.globals)
    context.update({'positions': positions})
    return render(request, 'polls/vote.html', context)