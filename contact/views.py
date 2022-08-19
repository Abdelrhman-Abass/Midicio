from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

def index(request):

    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(subject, message,settings.EMAIL_HOST_USER,
        [email],)

        return render(request, 'email_done.html' , {})

    return render(request, 'contact.html' , {})
# Create your views here.


