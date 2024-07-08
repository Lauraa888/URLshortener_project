from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLForm
from .models import URL
import string, random
from django.http import HttpResponse
import pyshorteners


def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    while URL.objects.filter(short_url=short_url).exists():
        short_url = ''.join(random.choices(characters, k=6))
    return short_url


def index(request):
    form = URLForm()
    if request.method == 'POST':
        form = URLForm(request.POST)        
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            url, created = URL.objects.get_or_create(original_url=original_url)
            if created:
                url.short_url = 'http://127.0.0.1:8000/' + generate_short_url()
                url.save()
            return render(request, 'shortener/result.html', {'short_url': url.short_url})

    return render(request, 'shortener/index.html', {'form': form})


def redirect_short_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)

    
