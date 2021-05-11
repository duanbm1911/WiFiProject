from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from main.forms import *
from main.models import *
from django.core.mail import send_mail
from django.conf import settings
from main.unifi_client import UnifiClient
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
import random
import time


def guest_default_portal(request):
    try:
        if request.method == "GET":
            form = UserInformationForm
            ssid = request.GET.get("ssid")
            client = request.GET.get("id")
            ap = request.GET.get("ap")
            data = {
                "form": form,
                "ssid": ssid.upper(),
                "client": client.lower(),
                "ap": ap.lower(),
            }
            count_client = UserInformation.objects.filter(
                device_mac_address=client
            ).count()
            if count_client == 0:
                return render(
                    request, template_name="guest_client_register.html", context=data
                )
            else:
                Model = UserInformation.objects.get(device_mac_address=client)
                client_status = Model.status
                if client_status == "DEACTIVE":
                    return render(
                        request, template_name="guest_confirm_code.html", context=data
                    )
            return render(request, template_name="guest_welcome.html", context=data)
        elif request.method == "POST":
            form_data = UserInformationForm(request.POST)
            client = form_data["device_mac_address"].value()
            ap = form_data["ap_mac_address"].value()
            if form_data.is_valid():
                form_data.save()
                client = form_data.cleaned_data["device_mac_address"]
                Model = UserInformation.objects.get(device_mac_address=client)
                email = Model.email
                code = random.randint(100000, 999999)
                Model.code = code
                Model.save()
                data = {
                    "client": client,
                    "ap": ap,
                }
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
                return render(
                    request, template_name="guest_confirm_code.html", context=data
                )
            else:
                data = {"form": form_data, "client": client, "ap": ap}
                return render(
                    request, template_name="guest_client_register.html", context=data
                )
    except Exception as error:
        return HttpResponse(error)


@login_required
def guest_client_connections(request):
    try:
        if request.method == "GET":
            clients = UnifiClient().get_client_detail_information()
            data = {"clients": clients}
            return render(
                request, template_name="guest_client_connections.html", context=data
            )
    except Exception as error:
        return HttpResponse(error)


@login_required
def guest_client_list(request):
    try:
        if request.method == "GET":
            clients = UserInformation.objects.order_by("email")
            data = {"clients": clients}
            return render(request, template_name="guest_client_list.html", context=data)

    except Exception as error:
        return HttpResponse(error)


@login_required
def home(request):
    try:
        if request.method == "GET":
            return render(request, template_name="home.html")

    except Exception as error:
        return HttpResponse(error)


class UpdateUserInformation(UpdateView):
    model = UserInformation
    form_class = UserInformationFormUpdate
    template_name = "update_user_information.html"
    success_url = "/guest/list"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self, **kwargs):
        return UserInformation.objects.get(id=self.kwargs["id"])

    def form_valid(self, form):
        if form.is_valid():
            client = form["device_mac_address"].value()
            bw_upload = form["bw_upload"].value()
            bw_download = form["bw_download"].value()
            time_used = form["time_used"].value()
            UnifiClient().set_bw_client(client, time_used, bw_upload, bw_download)
        return super().form_valid(form)


class StudentInformationList(ListView):
    model = StudentInformation
    context_object_name = "students"
    template_name = "student_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
