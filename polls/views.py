from django.http import HttpResponse


def index(request):
    from django.http import JsonResponse
    import json
    # my_json = json.loads(request.body)
    body_unicode = request.body.decode('utf-8')
    # my_json = json.loads(body_unicode)

    # response_dict = {}
    # for key in my_json:
    #     response_dict['key'] = key
    #     response_dict['value'] = my_json[key]
    # return JsonResponse(response_dict)
    from urllib import parse
    parse.unquote(body_unicode)
    response_dict = {}
    # response_dict["body"] = request.body
    response_dict['decoded_body'] = body_unicode
    return JsonResponse(response_dict)
