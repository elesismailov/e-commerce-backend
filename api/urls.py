from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<str:slug>/', views.ProductView.as_view()),


    path('cart/', views.CartView.as_view()),


    path('orders/', views.OrdersView.as_view()),
    path('orders/<int:order_id>/', views.OrderView.as_view()),
    path('orders/<int:order_id>/shipment/', views.OrderShipmentView.as_view()),

    # list all categories
    path('categories/', views.CategoryList.as_view()),

    # info about a category
    path('categories/<str:slug>/', views.CategoryView.as_view()),

    # list products of categories
    path('categories/<str:slug>/products/', views.CategoryProducts.as_view()),

    path('sign-up/', views.sign_up),
    path('log-in/', views.log_in),
]

urlpatterns = format_suffix_patterns(urlpatterns)

