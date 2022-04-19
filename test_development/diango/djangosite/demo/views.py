from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("<h1>hello django 666</h1>")


def home(request):
    return HttpResponse("这里是主页面")
