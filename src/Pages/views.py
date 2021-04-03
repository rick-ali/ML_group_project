from django.http import HttpResponse
from django.shortcuts import render

from .models import User

# Create your views here.
def home_view(request, *args, **kwargs):
    #print(request.user)
    #return HttpResponse("<h1>hello world</h1>")
    return render(request, "home.html", {})

def learn_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Learning page</h1>")
    return render(request, "learn.html", {})

def signIn_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Sign in page</h1>")
    return render(request, "signIn.html", {})

def signOut_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Working Page</h1>")
    return render(request, "signOut.html", {})

def signUp_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Working Page</h1>")
    return render(request, "signUp.html", {})

def faq_view(request, *args, **kwargs):
    #return HttpResponse("<h1>FAQ Page</h1>")
    return render(request, "faq.html", {})

def user_data_view(request):
    obj = User.objects.get(id=1)
    context = {
        'firstname': obj.firstname,
        'surname': obj.surname,
        'email': obj.email
    }
    return render(request, "user/data.html", context)

def choosing_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Choosing Page</h1>")
    return render(request, "choosing.html", {})
