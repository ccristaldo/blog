'''
from django.shortcuts import render

# Create your views here.
def Posts_list(request):
    return render(request,'posts/posts_list.html')
'''

from django.shortcuts import render
from django.utils import timezone
from .models import Post

def Posts_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'posts/posts_list.html', {'posts': posts})
