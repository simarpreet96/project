from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Img
from .forms import *
from django.http import HttpResponse 

#def doc_list(request):
    #return render(request, 'task/doc_list.html')    

def image_view(request): 
  
    if request.method == 'POST': 
        form = ImgForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('task:success') 
    else: 
        form = ImgForm() 
    return render(request, 'task/doc_list.html', {'form' : form}) 
  
def success(request): 
    return render(request, 'task/base.html')