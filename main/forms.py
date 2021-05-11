from django.forms import ModelForm
from django import forms
from main.models import *
import random

class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = [
            "email",
            "name",
            "classmate",
            "device_mac_address",
            "ap_mac_address",
            "phone",
            "device_type",
            "device_model",
        ]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        count_email = UserInformation.objects.filter(email=email.lower()).count()
        if count_email >= 2:
            raise forms.ValidationError("Vượt quá số thiết bị đăng ký với email này")
        # elif "student.vlute.edu.vn" not in email or 'vlute.edu.vn' not in email:
        elif '@' not in email:
            raise forms.ValidationError("Định dạng email không hợp lệ vui lòng thử lại")
        else:
            return email.lower()

    def clean_device_mac_address(self):
        device_mac_address = self.cleaned_data.get("device_mac_address")
        count_device_mac_address = UserInformation.objects.filter(device_mac_address=device_mac_address).count()
        if count_device_mac_address != 0:
            raise forms.ValidationError("Thiết bị đã được đăng ký, vui lòng thử lại")
        else:
            return device_mac_address

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if len(str(phone)) !=9:
            raise forms.ValidationError("Số điện thoại không hợp lệ, vui lòng thử lại")
        else:
            return phone

class UserInformationFormUpdate(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = [
            'device_mac_address',
            'bw_upload',
            'bw_download',
            'time_used'
        ]

