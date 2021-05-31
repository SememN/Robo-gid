from django.shortcuts import render
from django.utils.html import format_html

from . import services as servc


def load_it_page(request):
    creds = servc.get_creds('it')
    return render(request, 'kvants/base_kvant.html', {'kvant': creds[0],
                                                      'courses_list': creds[1],
                                                      })


def load_aero_page(request):
    creds = servc.get_creds('aero')
    return render(request, 'kvants/base_kvant.html', {'kvant': creds[0],
                                                      'courses_list': creds[1],
                                                      })


def load_auto_page(request):
    creds = servc.get_creds('auto')
    return render(request, 'kvants/base_kvant.html', {'kvant': creds[0],
                                                      'courses_list': creds[1],
                                                      })


def load_design_page(request):
    creds = servc.get_creds('design')
    return render(request, 'kvants/base_kvant.html', {'kvant': creds[0],
                                                      'courses_list': creds[1],
                                                      })


def load_robo_page(request):
    creds = servc.get_creds('robo')
    return render(request, 'kvants/base_kvant.html', {'kvant': creds[0],
                                                      'courses_list': creds[1],
                                                      })


def load_hi_tech_page(request):
    creds = servc.get_creds('hi-tech')
    return render(request, 'kvants/base_kvant.html', {'kvant': creds[0],
                                                      'courses_list': creds[1],
                                                      })
