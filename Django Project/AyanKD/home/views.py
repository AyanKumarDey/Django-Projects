from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    # context = {
    #     'variable':"This is the value which is sent by the user"
    # }
    messages.success(request,'This is a test message')
    return render(request,'index.html')
    # return HttpResponse("This is Homepage")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is About Page")

def service(request):
    return render(request,'services.html')
    # return HttpResponse("This is Service Page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact = Contact(name=name , email=email , phone=phone , description=description , date=datetime.today())
        contact.save()
        messages.success(request,'Your Form Is Submitted')
    return  render(request,'contact.html')
    # return HttpResponse("This is Contact Page")