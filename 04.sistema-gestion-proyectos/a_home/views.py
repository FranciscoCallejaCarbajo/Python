from django.shortcuts import render
from django.contrib.auth.models import User

def home_view(request):
    
    context = {
        
    }
    return render(request, 'index.html', context=context)
