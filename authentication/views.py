from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re
# Create your views here.

# regex for password validation
PASS_REGEX = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,35}$"


def signup(request):
    signup_context = {'passError': False, 'emailExist': False,
                      'currEmail': '', 'currFname': '', 'currLname': '', 'passErrorMessage': 'Password Error'}

    if request.method == 'POST':
        email = str(request.POST.get('email')).strip()
        fname = str(request.POST.get('fname')).strip()
        lname = str(request.POST.get('lname')).strip()
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm-password')

        signup_context['currEmail'] = email
        signup_context['currFname'] = fname
        signup_context['currLname'] = lname

        if User.objects.filter(email=email).exists() or User.objects.filter(username=email):
            signup_context['emailExist'] = True
            

            return render(request, "authentication/signup.html", signup_context)

        if pass1 != pass2:
            signup_context['passError'] = True
            signup_context['passErrorMessage'] = "Password doesn't match!"
            return render(request, "authentication/signup.html", signup_context)

        if not validatePassword(pass1):
            signup_context['passError'] = True
            signup_context['passErrorMessage'] = 'Enter a valid password!'
            return render(request, "authentication/signup.html", signup_context)

            

        newUser = User.objects.create_user(email, email, pass1)
        newUser.first_name = fname
        newUser.last_name = fname
        newUser.is_active = True
        newUser.save()
        if newUser is not None:
            login(request, newUser)
            return redirect('home')
    return render(request, "authentication/signup.html", signup_context)


def signin(request):
    login_context = {}
    if request.method == 'POST':
        email = str(request.POST.get('email')).strip()
        pass1 = request.POST.get('password')

        user = authenticate(username=email, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('home')

    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'authentication/login.html', login_context)


def signout(request):
    logout(request)
    return redirect('home')


# helper functions

def validatePassword(password):
    return True if re.match(PASS_REGEX, password) else False