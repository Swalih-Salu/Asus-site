from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def Home(req,c_slug=None):
    c_page=None
    Product_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        Product_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        Product_list=Product.objects.all().filter(available=True)
        
        
    paginator=Paginator(Product_list,4)
    try:
       page=int(req.GET.get('page',))
    except:
       page=1
    try:
       product=paginator.page(page)
    except(EmptyPage,InvalidPage):
       product=paginator.page(paginator.num_pages)  

    return render(req,'index.html',{"product":product,"cat":c_page})

def Details(req,id):
    data=Product.objects.get(id=id)
    return render(req,"details.html",{'data':data})

def Wishlist(req,id):
    data=Product.objects.get(id=id)
    return render(req,"wishlist.html",{'data':data})
