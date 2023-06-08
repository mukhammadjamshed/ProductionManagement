from django.urls import path
from .views import ProductMaterialAPIView

urlpatterns = [
    path('products/', ProductMaterialAPIView.as_view(), name='product-material-api'),
]
