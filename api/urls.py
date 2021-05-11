from django.urls import path, include
from api import views

urlpatterns = [
    path('email_verify_code', views.email_verify_code, name='email_verify_code'),
    path('request_send_code', views.request_send_code, name='request_send_code'),
    path('client_request_connect', views.client_request_connect, name='client_request_connect'),
    path('kick_out_client', views.kick_out_client, name='kick_out_client'),
    path('request_delete_client', views.request_delete_client, name='request_delete_client'),
    path('request_student_information', views.request_student_information, name='request_student_information'),
    path('request_list_student_auto_complete', views.request_list_student_auto_complete, name='request_list_student_auto_complete'),
    path('request_check_student_information', views.request_check_student_information, name='request_check_student_information')

]
