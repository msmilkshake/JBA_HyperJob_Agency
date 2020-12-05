from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from resume.models import Resume
from vacancy.models import Vacancy
from website.forms import CreateForm

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
        return render(
            request,
            'website/index.html',
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


class ProfileView(View):

    def get(self, request):
        create_form = CreateForm()
        action = 'resume'
        if request.user.is_staff:
            action = 'vacancy'
        return render(
            request,
            'website/profile.html',
            context={
                'user': request.user,
                'action': action,
                'create_form': create_form
            }
        )


class NewVacancy(View):
    def get(self, request):
        return redirect('/')

    def post(self, request):
        u = request.user
        if not u.is_staff or not u.is_authenticated:
            return HttpResponseForbidden()
        form = CreateForm(request.POST)
        if form.is_valid():
            Vacancy.objects.create(author=u, description=form.cleaned_data['description'])
        else:
            return HttpResponseForbidden()
        return redirect('/')


class NewResume(View):
    def get(self, request):
        return redirect('/')

    def post(self, request):
        u = request.user
        if u.is_staff or not u.is_authenticated:
            return HttpResponseForbidden()
        form = CreateForm(request.POST)
        if form.is_valid():
            Resume.objects.create(author=u, description=form.cleaned_data['description'])
        else:
            return HttpResponseForbidden()
        return redirect('/')
