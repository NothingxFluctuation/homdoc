from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ChestPainForm
# Create your views here.


def home(request):
    if request.method=='POST':
        chest_pain_form = ChestPainForm(request.POST)
        t = request.POST.get('t')
        tt = request.POST.get('tt')
        print('t',t,'tt',tt)
        if chest_pain_form.is_valid():
            b = chest_pain_form.save()
            b.age = b.age + " " + str(t)
            b.duration = b.duration + " " + str(tt)
            b.save()

            return HttpResponse("Form is submitted.")
        else:
            print(chest_pain_form.errors)
            return HttpResponse("Fill the form properly.")
    
    chest_pain_form = ChestPainForm(initial={'ch':'years','ch2':'hours'})
    return render(request, 'ind.html',{'chest_pain_form':chest_pain_form})


