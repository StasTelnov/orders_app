from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from stronghold.decorators import public
from .forms import CustomUserCreationForm


@public
def welcome(request):
    if 'next' in request.GET:
        if not request.user.is_authenticated():
            messages.error(request, "You're should login before continue.")
        else:
            messages.error(request, "Sorry, but you do not have permission for \
                                                                this action.")
    return render(request, 'accounts/welcome.html')


@public
def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    to = 'welcome'
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.success(request, "You're successfully sign in!")
            to = request.POST.get('next') or to
        else:
            messages.warning(request, "Sorry, but your account disabled.")
    else:
        messages.warning(request, "Invalid login.")
    return redirect(to)


def sing_out(request):
    logout(request)
    messages.success(request, "You're successfully sign out!")
    return redirect('welcome')


@public
def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
                messages.success(request, "You're successfully sign up!")
            else:
                messages.warning(request, "Sorry, but your account disabled \
                                                                        yet.")
            return redirect('welcome')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/sign_up.html', {'form': form})
