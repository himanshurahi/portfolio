from django.shortcuts import render, get_object_or_404

from .models import blog
# Create your views here.

def home(request):
    blogs = blog.objects
    return render(request,'blog_home.html',{'blogs':blogs})

def details(request, blog_id):
    blog_details = get_object_or_404(blog, pk=blog_id)
    return render(request, 'details.html',{'blog_detail':blog_details})
