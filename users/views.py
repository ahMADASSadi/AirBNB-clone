from django.shortcuts import render
from django.views.generic import View, FormView

from .forms import LoginForm


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = '/rooms/'
