from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import Product, Size, ProductFilter
# Create your views here.

def product_info(request, product_id):
    size_list = Size.objects.filter(product__id=product_id)
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/info.html', {'product': product, 'size_list': size_list})

def product_filter(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'product/filter.html', {'filter': f})