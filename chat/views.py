from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Profile
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib import messages

def frontpage(request):
    return render(request, 'chat/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'chat/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'chat/frontpage.html')


User = get_user_model()
