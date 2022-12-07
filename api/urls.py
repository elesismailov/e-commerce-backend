from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('sign-up/', views.sign_up),
    path('log-in/', views.log_in),
]

urlpatterns = format_suffix_patterns(urlpatterns)
