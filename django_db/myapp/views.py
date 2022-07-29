from django.shortcuts import render
from .models import post


# Create your views here.
def index(request):
    templatename = 'index.html'
    posts = post.objects.all().count
    context = {'posts': posts}
    return render(request, templatename, context)
