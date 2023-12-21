from django.shortcuts import render
from products.models import *

def products_page_view(request):
    cat = request.GET.get('cat')
    company = request.GET.get('company')
    color = request.GET.get('color')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    sort = request.GET.get('sort')

    products = ProductModel.objects.all().order_by('-pk')
    categories = CategoryModel.objects.all().order_by('-pk')
    companies = CompanyModel.objects.all().order_by('-pk')
    colors = ColorModel.objects.all().order_by('-pk')
    tags = TagModel.objects.all().order_by('-pk')

    if cat:
        products = products.filter(categories=cat)
    if company:
        products = products.filter(companies=company)
    if color:
        products = products.filter(colors=color)
    if tag:
        products = products.filter(tags=tag)
    if q:
        products = products.filter(title__icontains=q)
    if sort:
        if sort == "-price":
            products = products.order_by('price')
        elif sort == "price":
            products = products.order_by('-price')
    context = {
        "products": products,
        "categories": categories,
        "colors": colors,
        "tags": tags,
        "companies": companies
    }
    return render(request, 'product-list.html', context)