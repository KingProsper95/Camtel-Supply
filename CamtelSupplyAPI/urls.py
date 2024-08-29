from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

# importing all views
from .views.categoryView import *
from .views.entityView import *
from .views.productView import *
from .views.supplierView import *
from .views.orderView import *


urlpatterns = [

    #authentication
    path('auth/', obtain_auth_token),

    #category urls
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>', SingleCategoryView.as_view()),

    #product urls
    path('products/', ProductView.as_view()),
    path('products/<int:pk>', SingleProductView.as_view(), name='product-detail'),

    #entity urls
    path('entity/', EntityView.as_view()),
    path('entity/<int:pk>', SingleEntityView.as_view()),

    #supplier urls
    path('suppliers/', SupplierView.as_view()),
    path('suppliers/<int:pk>', SingleSupplierView.as_view()),


]