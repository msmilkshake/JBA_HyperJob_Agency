from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

menu = {
    'login': 'Login',
    'signup': 'Signup',
    'vacancies': 'Available Vacancies',
    'resumes': 'Available Resumes',
    'home': 'Your Profile'
}


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/index.html',
                      context={
                          'menu': menu,
                          'user': request.user
                      })


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'website/signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    success_url = ''
    template_name = 'website/login.html'
