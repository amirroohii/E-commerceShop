from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm,LoginForm
from .models import User


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request, 'accounts/sign_up.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data['email']
            user_password = register_form.cleaned_data['password']
            username = register_form.cleaned_data['username']
            user_first_name = register_form.cleaned_data['first_name']
            user_last_name = register_form.cleaned_data['last_name']
            user: bool = User.objects.filter(email=user_email, username=username).exists()
            if user:
                register_form.add_error('email', 'Email already registered.')
            else:
                new_user = User(
                    email=user_email,
                    first_name=user_first_name,
                    last_name=user_last_name,
                    username=username,
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login'))
        context = {'register_form': register_form}
        return render(request, 'accounts/sign_up.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                form.add_error('username', 'Invalid email,username or password.')
    return render(request, 'accounts/login_page.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))
