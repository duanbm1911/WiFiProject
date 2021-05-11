from django.contrib import admin
from main.models import *

# Register your models here.


class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('device_type',)


admin.site.register(DeviceType, DeviceTypeAdmin)


class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(UserInformation, UserInformationAdmin)


class StudentInformationAdmin(admin.ModelAdmin):
    list_display = ('student_code',)

admin.site.register(StudentInformation, StudentInformationAdmin)
