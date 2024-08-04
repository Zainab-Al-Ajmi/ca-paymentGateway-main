# Register your models here.
from django.contrib import admin
from .models import Course, DiscountCode, CourseRegistration, Sublevels

admin.site.register(Course)
admin.site.register(DiscountCode)
admin.site.register(CourseRegistration)
admin.site.register(Sublevels)