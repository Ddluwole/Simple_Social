from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import User
from django.urls import reverse_lazy
from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'Sign Up'
    #     return super().get_context_data(**kwargs)
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['username'].label = 'Display Name'
    #     form.fields['email'].label = 'Email Address'
    #     return form
    # def get_success_url(self):
    #     return reverse_lazy('login')
    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'Sign Up'
    #     return super().get_context_data(**kwargs)
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['username'].label = 'Display Name'
    #     form.fields['email'].label = 'Email Address'
    #     return form
    # def get_success_url(self):
    #     return reverse_lazy('login')
    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'Sign Up'
    #     return super().get_context_data(**kwargs)
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['username'].label = 'Display Name'
    #     form.fields['email'].label = 'Email Address'
    #     return form
    # def get_success_url(self):
    #     return reverse_lazy('login')
    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'Sign Up'
    #     return super().get_context_data(**kwargs)

