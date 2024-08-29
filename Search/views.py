from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from . import client
# Create your views here.
class SearchProductListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            query = request.GET.get('q')
            if not query:
                return Response('', status=400)
            results = client.perform_search(query)
            print(request.user.is_authenticated)
            return Response(results)
        return Response({"status" : "Can't perform this search you are not authenticated"},
                        status.HTTP_401_UNAUTHORIZED
                        )
