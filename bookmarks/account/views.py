from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


def user_login(request):
    # Check if request type is POST
    if request.method == 'POST':
        # Get user form data
        form = LoginForm(request.POST)
        # Validate form, if form not valid, return view with fields errors
        if form.is_valid():
            # Authenticate user
            cd = form.cleaned_data
            # Return user instance if user found
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    # Login user (put in session)
                    login(request, user)
                    return HttpResponse("Uwierzytelnienie zakończyło się sukcesem")
                else:
                    return HttpResponse("Konto jest zablokowane")
            else:
                return HttpResponse("Nieprawidłowe dane uwierzytelniające")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # Utworzenie profilu użytkownika
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if not getattr(request.user, "profile", None):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Zmiany zostały zapisane")
        else:
            messages.error(request, "Błąd - zmiany nie zostały zapisane")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
