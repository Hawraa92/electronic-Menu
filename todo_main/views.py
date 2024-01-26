from django.shortcuts import render
from .models import MenuItem  # Import your actual model

def home_view(request):
    context = {}
    return render(request, 'home.html', context)

def menu_view(request):  
    context = {}
    return render(request, 'menu.html', context)

def order_view(request):
    context = {}
    return render(request, 'order-online.html', context)

def contact_view(request):  
    context = {}
    return render(request, 'contact.html', context)

def gallery_view(request):  
    context = {}
    return render(request, 'gallery.html', context)

def signup_view(request):
    context = {}
    return render(request, 'signup.html', context)


def search_results(request):
    query = request.GET.get('query', '')
    results = MenuItem.objects.filter(name__icontains=query) if query else []  # Adjust the query based on your model and search field
    return render(request, 'search_results.html', {'results': results})
