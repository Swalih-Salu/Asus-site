from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('',views.Home,name='home'),
    path('<slug:c_slug>/',views.Home,name='prod_by_cat'),
    path('details/<int:id>/',views.Details,name='details'),
    path('wishlist/<int:id>/',views.Wishlist,name='wishlist'),
   
]
