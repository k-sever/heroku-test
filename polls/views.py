from django.http import HttpResponse


def index(request):
    from django.http import JsonResponse
    import json
    my_json = json.loads(request.body)
    response_dict = {}
    for key in my_json:
        response_dict['key'] = key
        response_dict['value'] = my_json[key]
    return JsonResponse(response_dict)