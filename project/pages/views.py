from django.shortcuts import render, HttpResponseRedirect
from .models import Login
from .forms import LoginForm
# from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {'name':'Sara', 'age':1234}
    return render(request, 'pages/index.html', context)
    # return HttpResponse('Hello, world! from pages')

def about(request):
    # return HttpResponse('about pages')
    if request.method == 'GET':
        return render(request, 'pages/about.html', {'lf':LoginForm} )

    data = LoginForm(request.POST)
    if data.is_valid():
        data.save()
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # temp = Login(username=username, password=password)
    # print(username, password)
    # temp.save()
    return render(request, 'pages/index.html')