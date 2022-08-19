from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Apointment , Doctor
from .forms import ApointmentForm
def makeapointment(request):
    apointment = Apointment.objects.all()

    if request.method == 'POST':
        form = ApointmentForm(request.POST ,request.FILES)
        if form.is_valid():
            myform = form.save()
            return render(request, 'apoint_done.html' , {})
            

    else:
        form = ApointmentForm()


    return render(request, 'makeapointment.html' , {'form':form})



