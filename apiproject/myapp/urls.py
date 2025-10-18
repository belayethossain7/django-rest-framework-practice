from django.urls import path
from myapp import views

urlpatterns = [
    path("myapp/", views.api_list),
    path("myapp/<int:pk>/", views.api_detail),
    
]

