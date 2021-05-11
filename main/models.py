from django.db import models


# Create your models here.


class DeviceType(models.Model):
    device_type = models.CharField(max_length=1000)

    def __str__(self):
        return self.device_type


class StudentInformation(models.Model):
    student_id = models.CharField(max_length=100)
    student_code = models.CharField(max_length=100)
    student_name = models.CharField(max_length=200)
    student_classmate = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100)

    def __str__(self):
        return self.student_code


class UserInformation(models.Model):
    email = models.CharField(max_length=1000, verbose_name="Địa chỉ email")
    name = models.CharField(max_length=1000, verbose_name="Họ và tên sinh viên")
    classmate = models.CharField(max_length=100, verbose_name="Khóa học/lớp học")
    phone = models.IntegerField(verbose_name="Số điện thoại đăng ký")
    device_mac_address = models.CharField(
        max_length=20, unique=True, verbose_name="Địa chỉ MAC của thiết bị"
    )
    bw_upload = models.IntegerField(
        default=10000, verbose_name="Băng thông upload (Kbps)"
    )
    bw_download = models.IntegerField(
        default=10000, verbose_name="Băng thông download (Kbps)"
    )
    time_used = models.IntegerField(default=60, verbose_name="Thời gian sử dụng (Phút)")
    ap_mac_address = models.CharField(max_length=20, verbose_name="Địa chỉ MAC của AP")
    device_type = models.ForeignKey(
        "DeviceType", on_delete=models.CASCADE, verbose_name="Loại thiết bị"
    )
    device_model = models.CharField(max_length=1000, verbose_name="Tên thiết bị")
    code = models.IntegerField(null=True)
    status = models.CharField(default="DEACTIVE", max_length=200)

    def __str__(self):
        return self.email
