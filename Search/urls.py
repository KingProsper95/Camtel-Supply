from django.urls import path
from .views import SearchListView

urlpatterns = [
    path('products/', SearchListView.as_view())
]