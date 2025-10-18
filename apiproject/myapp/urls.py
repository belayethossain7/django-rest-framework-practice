from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path("contacts/", views.ContactList.as_view()),
    path("contacts-details/<int:pk>/", views.ContactDetail.as_view()),
    path("gav/", views.BlogList.as_view(), name="contact-list"),
    path("gav-details/<int:pk>/", views.BlogDetail.as_view()),
    path("", views.api_root),
])

