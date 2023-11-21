from django.urls import path
from .views import import_from_excel,ProductListCreateView,ProductDetailView

urlpatterns = [
    path('import', import_from_excel, name='import_excel'),
    path('api/products', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    
]