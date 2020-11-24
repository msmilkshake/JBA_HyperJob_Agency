from django.shortcuts import render
from django.views import View

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
        return render(request, 'website/index.html', context={'menu': menu})
