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
import polls.models as models

# Create your views here.
def index(request):
    noInit = False
    showResults = False

    if 'init' not in request.session or any([ var not in request.session['init'] for var in globals.setDuringInit]):
        noInit = True
    # Replace with logic for checking if election is over
    if False:
        showResults = True
        positionList = bucket.fetchPositions(None)

    if 'token' in request.session.keys() or 'rollno' in request.session.keys():
        return HttpResponseRedirect(reverse('polls:logout'))
    context = globals.globals.copy()
    try:
        ongoingVal = models.ConfigVars.objects.get(varKey='ongoing').varVal
        publishedVal = models.ConfigVars.objects.get(varKey='publish').varVal
    except models.ConfigVars.DoesNotExist as e:
        util.initConfigTable()
        return HttpResponseRedirect(reverse('polls:index'))
    positionList = bucket.fetchPositions(None) # @todo: conditional
    context.update({'messages': messages.get_messages(request),'next':'index','noInit':noInit,'published':publishedVal, 'ongoing': ongoingVal, 'positions':positionList})
    return render(request, 'polls/index.html', context)


def verify(request):
    hideTextBox = False
    if request.POST:
        verifySignatureResult = auth.getVerifySignature(request.POST.get('token',''))
        print(verifySignatureResult)
        messages.add_message(
            request, messages.INFO if verifySignatureResult['status'] else messages.ERROR,
            verifySignatureResult['data']
        )
        if verifySignatureResult['status']:
            hideTextBox = True
    context = globals.globals.copy()
    context.update({'messages': messages.get_messages(request),'next':'verify','hideTextBox':hideTextBox})
    return render(request, 'polls/index.html', context)


def init(request):
    messageList = []
    # print(type(request.POST['name']))
    if request.POST:
        try:
            if all([request.POST.get(var,'') !=  '' for var in globals.setDuringInit]):
                if request.POST.get('clientKey','') == globals.clientKey:
                    request.session['init'] = { var : request.POST.get(var,'') for var in globals.setDuringInit}
                    return HttpResponseRedirect(reverse('polls:index'))
                else:
                    messageList.append('Invalid client key.')
            else:
                messageList.append('Please select one option.')
        except IndexError as e:
            print(e)
            pass
    context = {}
    context.update(globals.globals)
    # ['hostel':{'id':'a','name':'a'}]
    vars = [ {"name" : var, "options" : [{'id':option[0],'name':option[1]} for option in globals.globals[var]]} for var in globals.setDuringInit]
    context.update({'variables':vars})
    print(vars)
    messageList.extend(messages.get_messages(request))
    context.update({'messages': messageList,'next':'init'})
    
    return render(request, 'polls/init.html', context)


def login(request):
    # checks if initialisation is done and all required init variables are set.
    if 'init' not in request.session or any([ var not in request.session['init'] for var in globals.setDuringInit]):
        return HttpResponseRedirect(reverse('polls:init'))
    
    redirectIfNotOngoing(request)
    
    messageList = []
    if request.POST:
        # print(request.POST)
        try:
            # Attempt authentication
            authResult =  auth.authenticate(request.POST.get('name',''),request.POST.get('password',''),request.POST.get('token',''))
            if authResult == True:
                request.session['token'] = request.POST.get('token','')
                request.session['rollno'] = request.POST.get('name','') # @todo: rollno
                request.session['webmail'] = request.POST.get('webmail','')
                # @initparams
                bucketProcess = bucket.process(request.POST.get('name',''),request.session['init']['hostels'],request.session['init']['gender'])

                if not bucketProcess['status']:
                    messageList.append(bucketProcess['data'])
                else:
                    request.session['bucket'] = bucketProcess['data']
                    print('Authenticated!')
                    return HttpResponseRedirect(reverse('polls:vote'))
            else:
                messageList.append(authResult)
        except KeyError as e:
            messageList.append('Error')
            print(e)
            # pass
    
    context = {}
    context.update(globals.globals)
    messageList.extend(messages.get_messages(request))
    context.update({'messages': messageList,'next':'login'})
    # print(context)
    return render(request, 'polls/index.html', context)


def vote(request):

    redirectIfNotOngoing(request)

    # Not authenticated
    messageList = []
    if 'token' not in request.session.keys() and 'rollno' not in request.session.keys():
        messages.add_message(request, messages.ERROR, 'Please log-in before voting.')
        return HttpResponseRedirect(reverse('polls:login'))
    if request.POST:
        voteResult = votelib.storeVote(request)
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
    # empty these session variables on logout
    for sessionVar in ['token','rollno','bucket']:
        if sessionVar in request.session:
            del request.session[sessionVar]
    return HttpResponseRedirect(reverse('polls:index'))

def redirectIfNotOngoing(request):
    try:
        ongoingVal = models.ConfigVars.objects.get(varKey='ongoing').varVal
    except models.ConfigVars.DoesNotExist as e:
        util.initConfigTable()
        return HttpResponseRedirect(reverse('polls:login'))
    if ongoingVal == 0:
        messages.add_message(request, messages.INFO, 'The poll is not in progress, logging-in. You can not log-in or vote now.')
        return HttpResponseRedirect(reverse('polls:index'))
