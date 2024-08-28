from django.urls import path
from .views import SearchProductListView

urlpatterns = [
    path('products/', SearchProductListView.as_view())
]