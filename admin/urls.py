from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from admin import views

urlpatterns = [
    path('', views.IndexView.as_view()),

    path('products/', views.ProductsView.as_view()),
    path('products/<str:slug>/', views.ProductView.as_view()),
    path('categories/', views.CategoriesView.as_view()),
    path('categories/<str:slug>/', views.CategoryView.as_view()),

    path('orders/by-status-code/<str:slug>/', views.OrdersView.as_view()),
    path('orders/<int:order_id>/', views.OrderView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

