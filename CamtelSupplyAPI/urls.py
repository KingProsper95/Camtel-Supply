from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('category/', views.CategoryView.as_view()),
    path('category/<int:pk>', views.SingleCategoryView.as_view()),
    path('products/', views.ProductView.as_view(), name='product-list'),
    path('products/<int:pk>', views.SingleProductView.as_view(), name='product-detail'),
    path('suppliers/', views.SupplierView.as_view()),
    path('suppliers/<int:pk>', views.SingleSupplierView.as_view()),
    path('entity/', views.EntityView.as_view()),
    path('entity/<int:pk>', views.SingleEntityView.as_view()),
]