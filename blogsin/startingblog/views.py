from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post
from .forms import PostForm
# Create your views here.
def home(request):
    return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post

    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    # form_class = BlogForm
    login_url = '/home'
    template_name = 'update_post.html'
    fields = '__all__'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy('update', kwargs={'pk': blog_pk})
        return url
    
    def form_valid(self, form):
        messages.success(self.request, "The post has been updated successfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Failed to update the post. Please check the process again!")
        return super().form_invalid(form)
        
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('home')
    login_url = '/home'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "The post has been deleted!")
        return super().delete(request, *args, **kwargs)

