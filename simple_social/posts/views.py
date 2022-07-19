from django.contrib import messages
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from braces.views import SelectRelatedMixin
from requests import delete
from . import models, forms

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class PostList(SelectRelatedMixin, ListView):
    model=models.Posts
    select_related = ('user', 'group')

class UserPost(ListView):
    model = models.Posts
    template_name= 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact= self.kwargs.get('username'))

        except User.DoesNotExist:
            raise Http404

        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user']= self.post_user
        return super().get_context_data(**kwargs)

class PostDetail(SelectRelatedMixin, DetailView):
    model = models.Posts
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    fields = ('message', 'group')
    model = models.Posts

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = models.Posts
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
