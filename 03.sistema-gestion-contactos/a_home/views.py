from django.shortcuts import render
from django.contrib.auth.models import User

def home_view(request):
    usuarios =  list(User.objects.all())
    context = {
        "users": usuarios
    }
    return render(request, 'index.html', context=context)
