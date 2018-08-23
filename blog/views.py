from django.http import HttpResponse
from django.template import loader
from .models import Post

from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


#def post_list(request):
#   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#   template = loader.get_template('blog/post_list.html')
#   context = {
#      'name': "juan manuel",
#   }
#  return HttpResponse(template.render(context, request))
