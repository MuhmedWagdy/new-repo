from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from .forms import ProductAddForm
from .cart import Cart
from django.views.decorators.http import require_POST


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = ProductAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect('cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')
    
def cart_detail(request):
    cart = Cart(request)
    return render(request, '../templates/base/cart_detail.html', {'cart': cart})
