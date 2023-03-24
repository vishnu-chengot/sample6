from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'customer/home.html')

def login(request):
    return render(request,'customer/login.html')


def javascript(request):
    return render(request,'customer/javascript.html')

def baabtra(request):
    return render(request,'customer/baabtra.html')  


def javascript1(request):
    return render(request,'customer/javascript1.html')


def dom(request):
    return render(request,'customer/dom.html')
     
def domexample(request):
    return render(request,'customer/domexample.html')


def todoapp(request):
    return render(request,'customer/todoapp.html')

def calculator(request):
    return render(request,'customer/calculator.html')

def student(request):
    return render(request,'customer/student.html')

def jquery(request):
    return render(request,'customer/jquery.html')

def newpage(request):
    return render(request,'customer/newpage.html')


def listNew(request):
    return render(request,'customer/listNew.html') 

def calculator1(request):
    return render(request,'customer/calculator1.html')

def jquery1(request):
    return render(request,'customer/jquery1.html')

def jqueryform(request):
    return render(request,'customer/jqueryform.html')

def jqueryformwork(request):
    return render(request,'customer/jqueryformwork.html')

def jqueryslider(request):
    return render(request,'customer/jqueryslider.html')

def jqueryslider1(request):
    return render(request,'customer/jqueryslider1.html')


def jqueryslider2(request):
    return render(request,'customer/jqueryslider2.html')

def snakegame(request):
    return render(request,'customer/snakegame.html')