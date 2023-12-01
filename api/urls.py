from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'Category', CategoryViewSet)
router.register(r'Items', ItemViewSet)

urlpatterns = [
    # ... other urlpatterns ...
    path('', include(router.urls)),
]
