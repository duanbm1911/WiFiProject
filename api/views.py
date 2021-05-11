from django.shortcuts import *
from django.http import JsonResponse, HttpResponse
from main.models import *
from django.core.mail import send_mail
from django.conf import settings
import random
import json
import requests
import time
from datetime import datetime
from main.unifi_client import UnifiClient

# Create your views here.


def kick_out_client(request):
    try:
        if request.is_ajax():
            client_mac = request.GET.get("client_mac")
            kick_out_client = UnifiClient().unauthorize_guest(client_mac)
            time.sleep(3)
            data = {"status": "OK", "msg": "Kick-out thành công "}
            return JsonResponse(data)
    except Exception as error:
        return HttpResponse(error)


def client_request_connect(request):
    try:
        if request.is_ajax():
            client = request.GET.get("client")
            Model = UserInformation.objects.get(device_mac_address=client)
            check_client_status = Model.status
            bw_up = Model.bw_upload
            bw_down = Model.bw_download
            time_used = Model.time_used
            if check_client_status == "ACTIVE":
                unifi_client = UnifiClient()
                status = unifi_client.set_bw_client(client, time_used, bw_up, bw_down)
                time.sleep(5)
                if status == 200:
                    data = {"status": "OK", "msg": "Kết nối thành công!"}
                    return JsonResponse(data)
                else:
                    data = {"status": "NOK", "msg": "Wifi server đã có lỗi xảy ra"}
                    return JsonResponse(data)
    except Exception as error:
        return HttpResponse(error)


def email_verify_code(request):
    try:
        if request.is_ajax():
            code = request.GET.get("code")
            client = request.GET.get("client")
            Model = UserInformation.objects.get(device_mac_address=client)
            bw_up = Model.bw_upload
            bw_down = Model.bw_download
            time_used = Model.time_used
            check_code = Model.code
            if int(check_code) == int(code):
                Model.status = "ACTIVE"
                Model.save()
                client = Model.device_mac_address
                unifi_client = UnifiClient()
                status = unifi_client.set_bw_client(client, time_used, bw_up, bw_down)
                time.sleep(5)
                if status == 200:
                    data = {"status": "OK", "msg": "Đăng ký thành công!"}
                    return JsonResponse(data)
            else:
                data = {
                    "status": "NOK",
                    "msg": "Mã xác nhận sai, vui lòng thao tác lại",
                }
                return JsonResponse(data)
    except Exception as error:
        return HttpResponse(error)


def request_send_code(request):
    try:
        if request.is_ajax():
            client = request.GET.get("client")
            Model = UserInformation.objects.get(device_mac_address=client)
            email = Model.email
            code = random.randint(100000, 999999)
            Model.code = code
            Model.save()
            send_mail(
                "Số xác thực đăng ký WiFi VLUTE",
                "Xin chào người sử dụng\n\n"
                "Số xác thực đăng ký WiFi VLUTE của bạn là: "
                + str(code)
                + "\n\n"
                + "Nếu cần giúp đỡ, xin vui lòng liên hệ Khoa công nghệ thông tin qua các kênh sau đây: \n\n"
                + "- Địa chỉ: \n"
                + "    ◽️ Văn phòng khoa phòng C601\n"
                + "    ◽️ Trường Đại Học Sư Phạm Kỹ Thuật Vĩnh Long\n"
                + "- Phone: (+84) 02703828320\n"
                + "- Email: cit@vlute.edu.vn\n\n"
                + "TRÂN TRỌNG CÁM ƠN!",
                settings.EMAIL_HOST_USER,
                [
                    email,
                ],
            )
            data = {
                "status": "OK",
                "msg": "Gửi lại thành công, vui lòng kiểm tra email",
            }
            return JsonResponse(data)
    except Exception as error:
        return HttpResponse(error)


def request_delete_client(request):
    try:
        if request.is_ajax():
            client = request.GET.get("client")
            Model = UserInformation.objects.get(device_mac_address=client)
            Model.delete()
            data = {"status": "OK", "msg": "Xóa thiết bị thành công"}
            return JsonResponse(data)
    except Exception as error:
        return HttpResponse(error)


def request_student_information(request):
    try:
        if request.is_ajax():
            with requests.session() as Session:
                StudentInformation.objects.all().delete()
                student_code_range = range(17004001, 17004242)
                for student_code in student_code_range:
                    url = (
                        "https://ems.vlute.edu.vn/api/danhmuc/getsinhvienbykeyword/"
                        + str(student_code)
                    )
                    request_get = Session.get(url)
                    data = json.loads(request_get.content.decode("ascii"))[0]
                    model = StudentInformation(
                        student_id=str(data["id"]),
                        student_code=str(data["maSV"]),
                        student_name=str(data["ho"]) + " " + str(data["ten"]),
                        student_classmate=str(data["maLopCN"]),
                        student_email=str(data["maSV"]) + "@student.vlute.edu.vn",
                    )
                    model.save()
    except Exception as error:
        return HttpResponse(error)


def request_list_student_auto_complete(request):
    try:
        if request.is_ajax():
            student_name_list = list(
                StudentInformation.objects.values_list("student_name", flat=True)
            )
            student_classmate_list = list(
                set(
                    StudentInformation.objects.values_list(
                        "student_classmate", flat=True
                    )
                )
            )
            student_email_list = list(
                StudentInformation.objects.values_list("student_email", flat=True)
            )
            data = {
                "student_name_list": student_name_list,
                "student_classmate_list": student_classmate_list,
                "student_email_list": student_email_list,
            }
            return JsonResponse(data)
    except Exception as error:
        return HttpResponse(error)


def request_check_student_information(request):
    try:
        if request.is_ajax():
            student_email = request.GET.get("student_email")
            model = StudentInformation.objects.get(student_email=student_email)
            student_name = model.student_name
            student_classmate = model.student_classmate
            data = {
                "student_name": student_name,
                "student_classmate": student_classmate,
            }
            return JsonResponse(data)
    except Exception as error:
        return HttpResponse(error)
