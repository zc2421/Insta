from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Insta.models import Post
from django.urls import reverse_lazy

#test hello world page
class HelloWorld(TemplateView):
	template_name = "test.html"

#master -> details list view
class PostListView(ListView):
	model = Post
	template_name = 'index.html'


class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'


class PostCreateView(CreateView):
	model = Post 
	template_name = 'post_create.html'
	fields = '__all__'

class PostUpdateView(UpdateView):
	model = Post 
	fields = '__all__'
	template_name = 'post_edit.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


	

