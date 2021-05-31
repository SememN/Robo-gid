from django.shortcuts import render


def load_main_page(request):
    return render(request, 'main_page/main.html')