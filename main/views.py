from django.shortcuts import render

from kvant_projects import services


def load_main_page(request):
    return render(request, 'main_page/main.html', {'projects': services.get_projects()},)
