from django.contrib import admin

from .models import ItCourse, AutoCourse, AeroCourse, MathCourse, PromDesCourse, PromRoboCourse, HiTechCourse,\
    ChessCourse, ItDescription, AutoDescription, AeroDescription, MathDescription, PromDesDescription,\
    PromRoboDescription, HiTechDescription, ChessCDescription


admin.site.register(ItCourse)
admin.site.register(AutoCourse)
admin.site.register(AeroCourse)
admin.site.register(MathCourse)
admin.site.register(PromDesCourse)
admin.site.register(PromRoboCourse)
admin.site.register(HiTechCourse)
admin.site.register(ChessCourse)

admin.site.register(ItDescription)
admin.site.register(AutoDescription)
admin.site.register(AeroDescription)
admin.site.register(MathDescription)
admin.site.register(PromDesDescription)
admin.site.register(PromRoboDescription)
admin.site.register(HiTechDescription)
admin.site.register(ChessCDescription)
