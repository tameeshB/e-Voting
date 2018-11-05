from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.contrib import messages

import polls.auth as auth
import polls.util as util
import polls.globals as globals
import polls.bucket as bucket
import polls.vote as votelib

# Create your views here.
def index(request):
    context = globals.globals.copy()
    context.update({'messages': messages.get_messages(request),'next':'index'})
    return render(request, 'polls/index.html', context)

def login(request):
    print(request.POST)
    messageList = []
    # print(type(request.POST['name']))
    if request.POST:
        try:
            authResult =  auth.authenticate(request.POST['name'],request.POST['password'],request.POST['token'])
            if authResult == True:
                request.session['token'] = request.POST['token']
                request.session['rollno'] = request.POST['name'] # @todo: rollno
                # request.session['bucket'] = bucket.process(request.POST['name'],request.session['hostel'],request.session['gender'])
                bucketProcess = bucket.process(request.POST['name'],'BH1','M')
                if not bucketProcess['status']:
                    messageList.append(bucketProcess['data'])
                else:
                    request.session['bucket'] = bucketProcess['data']
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
    context.update({'messages': messageList,'next':'login'})
    
    return render(request, 'polls/index.html', context)

def vote(request):
    # Not authenticated
    messageList = []
    if 'token' not in request.session.keys() and 'rollno' not in request.session.keys():
        messages.add_message(request, messages.ERROR, 'Please log-in before voting.')
        return HttpResponseRedirect(reverse('polls:login'))
    if request.POST:
        voteResult = votelib.storeVote(request.POST)
        if voteResult['status']:
            messages.add_message(request, messages.SUCCESS, 'Thanks for voting!!')
            messages.add_message(request, messages.INFO, 'Your verification code is {} .'.format(voteResult['data']))
            return HttpResponseRedirect(reverse('polls:logout'))
        else:
            messageList.append(voteResult['data'])

    positionList = bucket.fetchPositions(request.session['bucket'])
    context = {}
    context.update(globals.globals)
    context.update({'positions': positionList,'user':request.session['rollno']})
    context.update({'messages': messageList,'next':'vote'})
    return render(request, 'polls/vote.html', context)



def logout(request):
    messages.add_message(request, messages.INFO, 'Successfully logged out.')
    del request.session['token']
    del request.session['rollno']
    del request.session['bucket']
    return HttpResponseRedirect(reverse('polls:index'))
