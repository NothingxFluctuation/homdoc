from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import ChestPainForm, LoginForm, RegistrationForm, EditForm
from .token import account_activation_token
from .models import Patient, Physician, Chest_Pain
from django.core.mail import EmailMessage, send_mail
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages



# Create your views here.

def user_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            em = cd['username']
            usr = User.objects.filter(email = em)
            if len(usr)>0:
                usr = User.objects.get(email = em)
                em = usr.username

            user = authenticate(request, username = em,password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    messages.success(request, "Authenticated Successfully.")
                    return redirect("/")
                else:
                    messages.error(request, "Disabled Account.")
                    return redirect('/login')
            else:
                messages.error(request, "Invalid login.")
                return redirect('/login')
    else:
        form = LoginForm()
        r_form = RegistrationForm()
    return render(request, 'login_register.html',{'form':form,'r_form':r_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('/login')



def user_registration(request):
    if request.method=='POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            #u_name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
            u_name = str(new_user.first_name) + '_' + str(new_user.last_name)
            u_name = u_name.replace(" ","_")
            chk_u = User.objects.filter(username = u_name)
            count =  0
            while len(chk_u)>0:
                #u_name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
                count += 1
                u_name = str(new_user.first_name) + '_' + str(new_user.last_name) + str(count)
                u_name = u_name.replace(" ","_")
                chk_u = User.objects.filter(username = u_name)
            
            new_user.username = u_name
            new_user.is_active = False
            new_user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('activate_account.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return render(request, 'register_done.html',{'new_user':new_user})
        else:
            r_form = RegistrationForm()
            form = LoginForm()
            return render(request,'login_register.html',{'r_form':r_form,'form':form})
    r_form = RegistrationForm()
    form = LoginForm()
    return render(request, 'login_register.html',{'r_form':r_form,'form':form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        p = Patient.objects.create(u=user)
        return redirect('/')
    else:
        return HttpResponse('Activation link is invalid!')




@login_required
def edit(request):
    ph = Physician.objects.filter(u=request.user)
    if len(ph)>0:
        msub = False
    else:
        msub = True
    if request.method=='POST':
        user_form = EditForm(instance = request.user, data = request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,"Changes saved successfully.")
            return redirect('/edit')
        else:
            messages.error(request,"Please enter correct values.")
            user_form = EditForm(instance = request.user)
    user_form = EditForm(instance = request.user)
    return render(request, 'new_edit.html',{'user_form':user_form, 'msub':msub})






@login_required
def home(request):
    if request.user.is_superuser:
        return redirect('admin/')

    ph = Physician.objects.filter(u=request.user)
    if len(ph)>0:
        msub = False
        submissions = Chest_Pain.objects.all().order_by('-created')
        return render(request, 'physician_profile.html',{'msub':msub,'submissions':submissions})
    
    if request.method=='POST':
        chest_pain_form = ChestPainForm(request.POST)
        t = request.POST.get('t')
        tt = request.POST.get('tt')
        print('t',t,'tt',tt)
        if chest_pain_form.is_valid():
            b = chest_pain_form.save()
            b.age = b.age + " " + str(t)
            b.duration = b.duration + " " + str(tt)
            p = Patient.objects.get(u=request.user)
            b.patient = p
            b.save()

            return redirect('my_submissions/')
        else:
            print(chest_pain_form.errors)
            return HttpResponse("Fill the form properly.")
    msub = True
    chest_pain_form = ChestPainForm(initial={'t':'Years','tt':'Hours'})
    return render(request, 'ind.html',{'chest_pain_form':chest_pain_form,'msub':msub})


@login_required
def submissions(request):
    p = Patient.objects.filter(u=request.user)
    if len(p)>0:
        p = Patient.objects.get(u=request.user)
    else:
        return HttpResponse("Log in from a patient account.")
    submissions = Chest_Pain.objects.filter(patient=p).order_by('-created')
    return render(request,'submissions.html',{'submissions':submissions})