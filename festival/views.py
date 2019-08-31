from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    return render(request,'index.html')

def plan(request):
    return render(request,'plan.html')

def lineup(request):
    return render(request,'lineup.html')

def food(request):
    blogs = Blog.objects
    return render(request,'food.html',{'blogs':blogs})