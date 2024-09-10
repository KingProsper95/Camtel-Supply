from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from . import client
# Create your views here.

class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            query = request.GET.get('q')
            index_name = request.GET.get('index')
            if not query or not index_name:
                return Response({"status":"invalid params"}, status.HTTP_400_BAD_REQUEST)
            results = client.perform_search(query, index_name)
            print(request.user.is_authenticated)
            return Response(results)
        return Response({"status" : "Can't perform this search you are not authenticated"},
                        status.HTTP_401_UNAUTHORIZED
                        )
    


