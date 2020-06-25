from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'malin/index.html')

def about(request):
    return render(request, 'malin/about.html')

def contact(request):
    return render(request, 'malin/contact.html')

def blog_detail(request):
    return render(request, 'malin/blog_detail.html')

def product(request):
    return render(request, 'malin/product.html')

def product_detail(request):
    return render(request, 'malin/product_detail.html')

def blog(request):
    return render(request, 'malin/blog.html')

def cart(request):
    return render(request, 'malin/cart.html')

def faq(request):
    return render(request, 'malin/faq.html')