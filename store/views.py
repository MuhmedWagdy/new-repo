from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import ProductAddForm

# Create your views here.


def product_list(request, category_slug=None):
    form = ProductAddForm()
    categories = Category.objects.all()
    products = Product.objects.filter(avaliable=True)
    category = None

    if category_slug:
        try:
            category = Category.objects.get(slug=category_slug)
        except:
            return render(request, 'base/404.html')

        products = category.products.filter(avaliable=True)

    return render(request, 'core/home.html', {'categories': categories, 'products': products, 'category': category, 'form': form})


def product_detail(request, id, slug):
    form = ProductAddForm()
    product = get_object_or_404(Product, id=id, slug=slug, avaliable=True)

    return render(request, '../templates/base/product_detail.html', {'product': product, 'form': form})
