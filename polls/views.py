from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
import polls.auth as auth
import polls.util as util
import polls.globals as globals

# Create your views here.
def index(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(globals.globals, request))
def login(request):
    print(request.POST)
    # print(type(request.POST['name']))
    if request.POST:
        try:
            if auth.authenticate(request.POST['name'],request.POST['password'],request.POST['token']):
                request.session['token'] = request.POST['token']
                request.session['rollno'] = request.POST['name']
                return HttpResponseRedirect(reverse('polls:vote'))
        except KeyError:
            pass
        except MultiValueDictKeyError:
            pass
    context = {}
    context.update(globals.globals)
    context.update({'error':'Wrong Password'})
    
    return render(request, 'polls/index.html', context)

def vote(request):
    template = loader.get_template('polls/index.html')
    print(request.POST)
    if request.POST:
        try:
            if auth.authenticate(request.POST['name'][0],request.POST['password'][0],request.POST['token'][0]):
                request.session['token'] = request.POST['token'][0]
                request.session['rollno'] = request.POST['name'][0]
                return HttpResponse(template.render(globals.globals, request))
        except:
            pass
    return HttpResponseRedirect(reverse('polls:index'))
    # return HttpResponse(template.render(context, request))