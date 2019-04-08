from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

class homePageView(TemplateView):
	template_name = 'index.html'