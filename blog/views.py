from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from .models import Post
# Create your views here.

class IndexView():
	# template_name = 'blog/index.html'
	# context_object_name = 'posts'
	# def get_queryset(request):
	# 	return Post.objects.order_by('-create_date')[:5]
	def home(request):
		data ={
			'title':"Blog",
		    'posts':Post.objects.order_by('-create_date')[:5]
		}
		return 	render(request, 'blog/index.html', data)	
class Single():
	def single(request, post_slug):
	    try:
	        post = Post.objects.get(post_slug=post_slug)
	        #post = get_object_or_404(Post, post_slug=post_slug)
	    except Post.DoesNotExist:
	        raise Http404("Post não encontrado")
	    return render(request, 'blog/single.html', {'post': post})	
 