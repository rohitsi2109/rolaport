from django.shortcuts import render, HttpResponse
from myportfolio.models import Contact
from datetime import datetime
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('email')
        phone = request.POST.get('Phone')
        message = request.POST.get('Message')

                # Create a new Contact object and save it to the database
        new_contact = Contact(
        name=name,
        email = email,
        phone=phone,
        message = message,
        date=datetime.today()
        )
        new_contact.save()
    return render(request, 'index.html')
     # return render(request, 'contact.html')
     # return HttpResponse("this is home page")
def project(request):
    return render(request, 'projects.html')

# def server_error(request):
#     return render(request, '500.html', status=500)