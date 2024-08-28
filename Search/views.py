from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from . import client
# Create your views here.

class SearchProductListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if not query:
            return Response('', status=400)
        results = client.perform_search(query)
        return Response(results)