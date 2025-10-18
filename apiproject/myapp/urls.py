from django.urls import path
from django.urls import include
from myapp.views import ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
