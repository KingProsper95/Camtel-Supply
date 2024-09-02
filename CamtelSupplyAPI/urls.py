from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView

# importing all views
from .views.categoryView import *
from .views.entityView import *
from .views.productView import *
from .views.supplierView import *
from .views.orderView import *


urlpatterns = [

    #authentication
    path('auth/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #category urls
    path('categories/', CategoryView.as_view()),
    path('category/<int:pk>', SingleCategoryView.as_view()),

    #product urls
    path('products/', ProductView.as_view()),
    path('product/<int:pk>', SingleProductView.as_view(), name='product-detail'),

    #entity urls
    path('entities/', EntityView.as_view()),
    path('entity/<int:pk>', SingleEntityView.as_view()),

    #supplier urls
    path('suppliers/', SupplierView.as_view()),
    path('supplier/<int:pk>', SingleSupplierView.as_view()),

    #order urls
    path('orders/', OrderView.as_view()),
    path('order/<int:pk>', SingleOrderView.as_view(), name='order-detail'),


]