from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def person(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        telephone1 = request.POST.get('telephone1')
        telephone2 = request.POST.get('telephone2')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        street = request.POST.get('street')
        town = request.POST.get('town')
        postalcode = request.POST.get('postalcode')
        country = request.POST.get('country')
        creation_date = request.POST.get('creation_date')
        changed_date = request.POST.get('changed_date')
        person = Person(first_name=first_name, last_name=last_name, telephone1=telephone1, telephone2=telephone2,
                        email1=email1, email2=email2, street=street, town=town, postalcode=postalcode, country=country, 
                        creation_date=creation_date, changed_date=changed_date)
        person.save()
        # subject = "Person Detail"  
        # msg     = f"Name: {first_name} \nAddress:{country} \nMobile No:{phone}"
        # res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [email])
        return HttpResponse('ok')
    return render(request, 'myapp/person.html')


def persondetail(request):
    person = Person.objects.all()
    return render(request, 'myapp/persondetail.html', {'person':person})