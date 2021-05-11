from django.urls import path, include
from main import views
from main.views import *

urlpatterns = [
    path("guest/s/default/", views.guest_default_portal, name="guest_default_portal"),
    path(
        "guest/connections",
        views.guest_client_connections,
        name="guest_client_connections",
    ),
    path("guest/list", views.guest_client_list, name="guest_client_list"),
    path(
        "guest/list/<id>",
        views.UpdateUserInformation.as_view(),
        name="UpdateUserInformation",
    ),
    path(
        "student/list", StudentInformationList.as_view(), name="StudentInformationList"
    ),
    path("", views.home, name="home"),
]
