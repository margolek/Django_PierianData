from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from blog.models import Post,Comment
#Remember! reverse_lazy in CBV, reverse in FBV
from django.urls import reverse_lazy
from blog.forms import PostForm,CommentForm
#Transform function decortor into class decorator
from django.utils.decorators import method_decorator
from django.views.generic import (TemplateView,ListView,DetailView,
								  CreateView,UpdateView,DeleteView)

class AboutView(TemplateView):
	template_name = 'about.html'

class PostListView(ListView):
	model = Post

	#This allows me to use ORM dealing with generic views
	#lte --> less than or equal to 
	#https://docs.djangoproject.com/en/3.1/ref/models/querysets/
	def get_queryset(self):
		return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
	model = Post

#Evuivalent @login_required with function based view
@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
	login_url ='/login/'
	redirect_field_name = 'blog/post_detail.html'
	form_class = PostForm
	model = Post

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
	login_url ='/login/'
	redirect_field_name = 'blog/post_detail.html'
	form_class = PostForm
	model = Post

@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy('post_list')

@method_decorator(login_required, name='dispatch')
class DraftListView(ListView):
	login_url = '/login/'
	redirect_field_name = 'blog/post_list.html'
	model = Post

	#Queryset with unpublished post
	def get_query_set(self):
		return Post.objects.filter(published_date__isnull=True).order_by('created_date')

###################
###################

@login_required
def post_publish(request,pk):
	post = get_object_or_404(Post,pk=pk)
	post.publish()
	return redirect('post_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
	post = get_object_or_404(Post,pk=pk)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail',pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
	comment = get_object_or_404(Comment,pk=pk)
	comment.approve()
	return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
	comment = get_object_or_404(Comment,pk=pk)
	#Create separate variable for post_pk before remove it
	post_pk = comment.post.pk
	comment.delete()
	return redirect('post_detail',pk=post_pk)
