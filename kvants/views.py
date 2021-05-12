from django.shortcuts import render
from django.utils.html import format_html

from .models import ItCourse, AutoCourse, AeroCourse, MathCourse, PromDesCourse, PromRoboCourse, HiTechCourse,\
    ChessCourse, ItDescription, AutoDescription, AeroDescription, MathDescription, PromDesDescription,\
    PromRoboDescription, HiTechDescription, ChessCDescription


def load_it_page(request):
    courses = ItCourse.objects.all()
    description = ItDescription.objects.get(id=1)
    return render(request, 'kvants/base_kvant.html', {'courses_list': courses,
                                                      'kvant': description})


def load_aero_page(request):
    return render(request, 'kvants/base_kvant.html', {'title': aero_kvant.NAME,
                                                      'html_source': format_html(aero_kvant.HTML),
                                                      })


def load_auto_page(request):
    return render(request, 'kvants/base_kvant.html', {'title': auto_kvant.NAME,
                                                      'html_source': format_html(auto_kvant.HTML),
                                                      })


def load_design_page(request):
    return render(request, 'kvants/base_kvant.html', {'title': prom_design_kvant.NAME,
                                                      'html_source': format_html(prom_design_kvant.HTML),
                                                      })


def load_robo_page(request):
    return render(request, 'kvants/base_kvant.html', {'title': prom_robo_kvant.NAME,
                                                      'html_source': format_html(prom_robo_kvant.HTML),
                                                      })


def load_hi_tech_page(request):
    return render(request, 'kvants/base_kvant.html', {'title': hi_tech_kvant.NAME,
                                                      'html_source': format_html(hi_tech_kvant.HTML),
                                                      })
