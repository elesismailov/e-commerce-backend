from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from admin import views

urlpatterns = [
    path('', views.IndexView.as_view()),

    path('products/', views.ProductsView.as_view()),
    path('products/<str:slug>/', views.ProductView.as_view()),
    path('categories/', views.CategoriesView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

