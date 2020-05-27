from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class PagesHome(TemplateView):
    template_name = "pages/pageshome.html"
