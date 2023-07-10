from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView): #Class responsible for sending Homepage as response
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html'