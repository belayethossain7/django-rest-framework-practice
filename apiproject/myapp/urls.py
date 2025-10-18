from django.urls import path
from myapp import views

urlpatterns = [
    path("contacts/", views.ContactList.as_view()),
    path("contacts-details/<int:pk>/", views.ContactDetail.as_view()),
    path("gav/", views.BlogList.as_view()),
    path("gav-details/<int:pk>/", views.BlogDetail.as_view()),
]

