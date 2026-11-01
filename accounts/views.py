from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import (
    JobSeekerRegisterForm,
    EmployerRegisterForm
)


def register_jobseeker(request):

    if request.method == 'POST':
        form = JobSeekerRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_jobseeker = True
            user.save()

            login(request, user)
            return redirect('home')

    else:
        form = JobSeekerRegisterForm()

    return render(
        request,
        'accounts/register_jobseeker.html',
        {'form': form}
    )


def register_employer(request):

    if request.method == 'POST':
        form = EmployerRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_employer = True
            user.save()

            login(request, user)
            return redirect('home')

    else:
        form = EmployerRegisterForm()

    return render(
        request,
        'accounts/register_employer.html',
        {'form': form}
    )


def user_login(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()

            login(request, user)

            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


def user_logout(request):
    logout(request)
    return redirect('home')