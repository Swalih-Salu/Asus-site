from django.shortcuts import render
from ShopApp.models import Product
from django.db.models import Q
# Create your views here.
def Search(request):
    product=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        product=Product.objects.all().filter(Q(name__contains=query))
    return render(request,'search.html',{'query':query,'product':product})
