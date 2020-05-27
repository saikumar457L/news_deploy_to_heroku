from django.shortcuts import render

from .forms import CustomUserCreationForm
from django.views.generic import CreateView,TemplateView

from django.urls import reverse_lazy, reverse
# Create your views here.

class HomePage(TemplateView):
    template_name = "users/home.html"

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")
