from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Insta.models import Post, Like, InstaUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from Insta.forms import CustomerUserCreationForm
from annoying.decorators import ajax_request

#test hello world page
class HelloWorld(TemplateView):
	template_name = "test.html"

#Create a list view
class PostListView(ListView):
	model = Post
	template_name = 'index.html'
	# login_url = 'login'

    
	
# View post details
class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'


# View User Details
class UserDetailView(DetailView):
    model = InstaUser
    template_name = 'user_detail.html'


# User upload post
class PostCreateView(CreateView):
	model = Post 
	template_name = 'post_create.html'
	fields = '__all__'

# Update a post
class PostUpdateView(UpdateView):
	model = Post 
	fields = '__all__'
	template_name = 'post_edit.html'

# Delete a post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')

#Create Sign Up View
class SignUp(CreateView):
	form_class = CustomerUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'	

@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }
