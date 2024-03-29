from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdateForm  # Importing both form classes
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def profileupdate(request):
    if request.method == 'POST':
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid():
            pform.save()
            return redirect('profile')
    else:
        pform = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/profileupdate.html', {'pform': pform})
