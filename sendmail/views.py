from django.shortcuts import render
from jinius import settings
# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            message = 'from: ' + from_email + f"({name})" + "\n" + form.cleaned_data['message']
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "sendmail/contact.html", {'form': form})

def successView(request):
    return render(request, "sendmail/success.html")