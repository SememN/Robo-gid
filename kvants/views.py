from django.shortcuts import render
from django.utils.html import format_html

from .models import ItCourse, AutoCourse, AeroCourse, PromDesCourse, PromRoboCourse, HiTechCourse,\
    ItDescription, AutoDescription, AeroDescription, PromDesDescription,\
    PromRoboDescription, HiTechDescription

def load_it_page(request):
    courses = ItCourse.objects.all()
    description = ItDescription.objects.get(id=1)
    return render(request, 'kvants/base_kvant.html', {'courses_list': courses,
                                                      'kvant': description})


def load_aero_page(request):
    courses = AeroCourse.objects.all()
    description = AeroDescription.objects.get(id=2)
    return render(request, 'kvants/base_kvant.html', {'courses_list': courses,
                                                      'kvant': description,
                                                      })


def load_auto_page(request):
    courses = AutoCourse.objects.all()
    description = AutoDescription.objects.get(id=3)
    return render(request, 'kvants/base_kvant.html', {'courses_list': courses,
                                                      'kvant': description,
                                                      })


def load_design_page(request):
    courses = PromDesCourse.objects.all()
    description = PromDesDescription.objects.get(id=5)
    return render(request, 'kvants/base_kvant.html', {'courses_list': courses,
                                                      'kvant': description,
                                                      })


def load_robo_page(request):
    courses = PromRoboCourse.objects.all()
    description = PromRoboDescription.objects.get(id=6)
    return render(request, 'kvants/base_kvant.html', {'courses_list': courses,
                                                      'kvant': description,
                                                      })


def load_hi_tech_page(request):
    courses = HiTechCourse.objects.all()
    description = HiTechDescription.objects.get(id=4)
    return render(request, 'kvants/base_kvant.html', {'courses_list': courses,
                                                      'kvant': description,
                                                      })
