from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

#definizione di una view

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # queryset
	return render(request, 'blog/post_list.html', {'posts':posts}) # template: blog/post_list.html

#request (quindi tutto quello che riceviamo dal nostro utente via internet)