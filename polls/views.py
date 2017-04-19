from django.http import HttpResponse


def index(request):
    from django.http import JsonResponse
    return JsonResponse({'blah':'polls-hahaha'})