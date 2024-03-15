from typing import Any
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Blog
from .forms import BlogForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class BlogListView(ListView):
    model = Blog
    paginate_by = 5
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    # fields = ['content',]
    success_url = reverse_lazy('index')
    login_url = '/login'

    def form_valid(self, form):
        messages.success(self.request, "A new post has been saved!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Failed to save the post. Please check the process again!')
        return super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    login_url = '/login'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy('detail', kwargs={'pk': blog_pk})
        return url
    
    def form_valid(self, form):
        messages.success(self.request, "The post has been updated successfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Failed to update the post. Please checke the process again!")
        return super().form_invalid(form)
        
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('index')
    login_url = '/login'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "The post has been deleted!")
        return super().delete(request, *args, **kwargs)

