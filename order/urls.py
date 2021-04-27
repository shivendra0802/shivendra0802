from django.urls import path, include
from order import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('slogin/', views.staff_login, name='stafflogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cart/', views.add_to_cart, name='cart'),
    path('logout/', views.user_logout, name='logout'),
    path('show_pro/<int:id>/', views.show_product, name='show_product'),
    path('show_cart', views.show_cart, name='showcart'),
    path('buy_now', views.buy_now, name='buynow'),
    path('dash/', views.up_dash, name='dash'),
    path('addcat/', views.add_category, name='addcat'),
    path('delcat/', views.delete_category, name='delcat'),
    path('logout/', views.user_logout, name='logout'),
    path('base/', views.base, name='base'),
]
