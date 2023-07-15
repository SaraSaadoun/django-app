from django.shortcuts import render
from .models import Product
# Create your views here.
def product(request):
    context = {
        'product': Product.objects.get(id=1)
    }
    return render(request, 'products/product.html', context)

def products(request):
    all_products = Product.objects.all()
    # filtered_products = all_products.filter(price=10)
    # filtered_products = all_products.filter(price__exact=10)
    # filtered_products = all_products.filter(price__contains=10)
    # filtered_products = all_products.filter(price__in=[10, 100, 500])
    filtered_products = all_products.filter(price__range=[10, 500])
    # filtered_products = all_products.exclude(price=10)
    ordered_products = filtered_products.order_by('name')
    products_num = str(ordered_products.count())
    final_products = {'productsNo':products_num,'products':ordered_products}
    return render(request, 'products/products.html', final_products)
