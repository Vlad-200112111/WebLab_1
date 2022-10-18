from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'