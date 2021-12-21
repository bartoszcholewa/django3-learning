from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    # Check if request type is POST
    if request.method == 'POST':
        # Get user form data
        form = LoginForm(request.POST)
        # Validate form, if form not valid, return view with fields errors
        if form.is_valid():
            # Authenticate user
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    # Login user
                    login(request, user)
                    return HttpResponse("Uwierzytelnienie zakończyło się sukcesem")
                else:
                    return HttpResponse("Konto jest zablokowane")
            else:
                return HttpResponse("Nieprawidłowe dane uwierzytelniające")
        else:
            form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


# Create your views here.
