from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1": "this is sent",
        "variable2": "second variable is also sent",
    }
    return render(request, 'index.html',context)
    # return HttpResponse("this is the homepage")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    if request.method == "POST":
        name =  request.POST.get('name')
        email =  request.POST.get('email')
        phone =  request.POST.get('phone')
        desc =  request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Profile details updated.')

    return render(request, 'services.html')

