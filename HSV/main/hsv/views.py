from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from .forms import ContactForm



def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Email:\n\t\t{}\n
        Subject:\n\t\t{}\n
        Message:\n\t\t{}\
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['subject'])
        
        send_mail('New Message', message, '',['<roykatiwa@gmail.com>'] ) 
        
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html')

def signin(request):
    return render(request, 'signin.html')

def services(request):
    return render(request, 'services.html')




