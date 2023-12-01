from django.urls import path

from .views import *

urlpatterns =[
    path('show_category/', get_category),
    path('save_category/', save_category),
    path('show_product/', get_product),
    path('save_category/', save_product)

]