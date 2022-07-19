from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Group,GroupMember
from . import models

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(group.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)


# from django.db import IntegrityError
# from django.db import models
# from django.shortcuts import HttpResponse, get_object_or_404
# from django.contrib.auth.mixins import (LoginRequiredMixin,
#                                          PermissionRequiredMixin)

# from django.contrib import messages
# from django.urls import reverse
# from django.views.generic import CreateView, TemplateView, DeleteView, DetailView,ListView, RedirectView
# from groups.models import Group, GroupMember

# # Create your views here.

# class CreateGroup(LoginRequiredMixin, CreateView):
#     model = Group
#     fields=("name", 'description')

# class SingleGroup(DetailView):
#     model = Group

# class ListGroups(ListView):
#     model = Group


# class JoinGroup(LoginRequiredMixin, RedirectView):

#     def get_redirect_url(self, *args, **kwargs):
#         return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

#     def get(self, request, *args, **kwargs):
#         group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

#         try:
#             GroupMember.objects.create(user=self.request.user, group=group)
#         except IntegrityError:
#             messages.warning(self.request, 'Warning, already a member!')

#         else:
#             messages.success(self.request, 'You are now a member!')

#         return super().get(request, *args, **kwargs)

# class LeaveGroup(LoginRequiredMixin, RedirectView):

#     def get_redirect_url(self, *args, **kwargs):
#         return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

#     def get(self, request, *args, **kwargs):

#         try:

#             membership = models.GroupMember.objects.filter(
#                 user=self.request.user,
#                 group__slug=self.kwargs.get("slug")
#             ).get()

#         except models.GroupMember.DoesNotExist:
#             messages.warning(
#                 self.request,
#                 "You can't leave this group because you aren't in it."
#             )
#         else:
#             membership.delete()
#             messages.success(
#                 self.request,
#                 "You have successfully left this group."
#             )
#         return super().get(request, *args, **kwargs)







