from django.db.models import Q
from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductSearchView(APIView):
    def get(self, request, format=None):
        query = self.request.query_params.get('search')
        if query:
            products = Product.objects.filter(Q(product__icontains=query) | Q(category__icontains = query))[:5]
        else:
            products =  Product.objects.none()
        serializer = ProductSerializer(products, many=True)
        response_data={"status":"success","results":serializer.data}
        return Response(response_data)

    def post(self, request, format=None):
        query = request.data.get('search')
        if query:
            products = Product.objects.filter(Q(product__icontains=query) | Q(category__icontains = query))[:5]
        else:
            products =  Product.objects.none()
        serializer = ProductSerializer(products, many=True)
        response_data={"status":"success","results":serializer.data}
        return Response(response_data)

