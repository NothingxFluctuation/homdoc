from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ChestPainForm
# Create your views here.


def home(request):
    if request.method=='POST':
        chest_pain_form = ChestPainForm(request.POST)
        if chest_pain_form.is_valid():
            chest_pain_form.save()
            return HttpResponse("Form is submitted.")
        else:
            return HttpResponse("Fill the form properly.")
    chest_pain_form = ChestPainForm()
    return render(request, 'ind.html',{'chest_pain_form':chest_pain_form})


