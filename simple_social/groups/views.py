from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                         PermissionRequiredMixin)
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, DeleteView, DetailView, UpdateView, ListView
from groups.models import Group, GroupMember
# Create your views here.

class CreateGroup(LoginRequiredMixin, CreateView):
    model = Group
    fields=("name", 'description')

class SingleGroup(DetailView):
    model = Group

class ListGroups(ListView):
    model = Group





