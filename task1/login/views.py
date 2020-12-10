from django.shortcuts import render
from django.http import HttpResponse
from .forms import login
# Create your views here.
def index(request):
    log=login()
    if request.method=="POST":
        log=login(request.POST)
        html='already submitted'
    else:
        html='welcome new user'
    return render(request,'login/index.html',{'html':html,'log':log})
