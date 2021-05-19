from django.contrib import admin

from .models import ItCourse, AutoCourse, AeroCourse, PromDesCourse, PromRoboCourse, HiTechCourse,\
    ItDescription, AutoDescription, AeroDescription, PromDesDescription,\
    PromRoboDescription, HiTechDescription

admin.site.register(ItCourse)
admin.site.register(AutoCourse)
admin.site.register(AeroCourse)
admin.site.register(PromDesCourse)
admin.site.register(PromRoboCourse)
admin.site.register(HiTechCourse)

admin.site.register(ItDescription)
admin.site.register(AutoDescription)
admin.site.register(AeroDescription)
admin.site.register(PromDesDescription)
admin.site.register(PromRoboDescription)
admin.site.register(HiTechDescription)
