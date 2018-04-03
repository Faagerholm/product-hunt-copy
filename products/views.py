from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'products/home.html')


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.POST['icon'] and request.POST['image']:

        else:
            return render(request, 'products/create.html', {'error': 'All fields are required'})
    else:
        return render(request, 'products/create.html')

