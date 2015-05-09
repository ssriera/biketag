from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, View
from django import http
from django.contrib.sites.models import Site
from django.contrib.auth import login
from django.core.mail import send_mail
from django.template.loader import render_to_string


class HomePage(TemplateView):
    template_name = "index.html"
