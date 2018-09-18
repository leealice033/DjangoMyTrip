from django.shortcuts import render
from matplotlib import pyplot as plt 
import pandas as pd
import os
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from .models import Post

import numpy as np

def hello_world(request):
    return render(request, 'hello_world.html', {'current_time':str(datetime.now()),})

def home(request):
	post_list = Post.objects.all()
	return render(request, 'home.html', {'post_list': post_list,})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'post.html', {'post': post,})

def getimage(request):
	x = np.arange(0, 2 * np.pi, 0.01)
	s = np.cos(x) ** 2
	fig,ax = plt.subplots()
	plt.plot(x, s)
	response = HttpResponse(content_type = 'image/jpeg')
	plt.savefig(response, format = 'png')
	return response

print("Hello!")