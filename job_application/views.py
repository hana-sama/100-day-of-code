from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from .emailing import TelegramBot
from django.contrib import messages

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name'].capitalize()
            last_name = form.cleaned_data['last_name'].capitalize()
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)

            bot = TelegramBot()
            bot.send(f'We hereby confirm that we have received an application from {first_name} {last_name} for jobs that will become available on {date}')

            messages.success(request, 'Form submitted successfully!')

    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')