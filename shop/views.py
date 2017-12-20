# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import Product,Category

# Create your views here.

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug :
        category = get_object_or_404(Category,slug = category_slug)
        products = products.filter(category=category)
    return render(request,"shop/product/list.html",{"products":products,"categories":categories,"category":category})


def product_detail(request,id,slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    #cart_product_form = CartAddProductForm()
    return render(request,"shop/product/detail.html",{"product":product})