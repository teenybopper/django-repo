from rest_framework import viewsets
from items.models import Category, Items
from .serializers import CategorySerializer, ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
