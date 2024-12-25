from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm,LoginForm
from .models import User


from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm

# View for handling user registration
class RegisterView(View):
    # Handle GET request to display the registration form
    def get(self, request):
        # Create an instance of the registration form
        register_form = RegisterForm()
        # Prepare the context with the form to be rendered
        context = {'register_form': register_form}
        # Render the sign-up template with the context
        return render(request, 'accounts/sign_up.html', context)

    # Handle POST request to process the registration form submission
    def post(self, request):
        # Create a form instance with the submitted data
        register_form = RegisterForm(request.POST)
        # Check if the form data is valid
        if register_form.is_valid():
            # Extract cleaned data from the form
            user_password = register_form.cleaned_data['password']
            username = register_form.cleaned_data['username']
            # Check if a user with the same username already exists
            user: bool = User.objects.filter(username=username).exists()
            if user:
                # Add an error to the form if the email is already registered
                register_form.add_error('email', 'Email already registered.')
            else:
                # Create a new user instance with the provided data
                new_user = User(
                    username=username,
                )
                # Set the password for the new user (hashed)
                new_user.set_password(user_password)
                # Save the new user to the database
                new_user.save()
                # Redirect to the login page after successful registration
                return redirect(reverse('login'))
        # If the form is not valid, render the sign-up template with errors
        context = {'register_form': register_form}
        return render(request, 'accounts/sign_up.html', context)


# View for handling user login
def login_view(request):
    # Create a form instance with the submitted data or None for GET requests
    form = LoginForm(request.POST or None)
    # Check if the request method is POST
    if request.method == 'POST':
        # Validate the form data
        if form.is_valid():
            # Extract username and password from the cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate the user with the provided credentials
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in if authentication is successful
                login(request, user)
                # Redirect to the home page after successful login
                return redirect(reverse('home'))
            else:
                # Add an error to the form if authentication fails
                form.add_error('username', 'Invalid email, username or password.')
    # Render the login page with the form (including any errors)
    return render(request, 'accounts/login_page.html', {'form': form})


# View for handling user logout
class LogoutView(View):
    # Handle GET request to log out the user
    def get(self, request):
        # Log out the user
        logout(request)
        # Redirect to the login page after logout
        return redirect(reverse('login'))