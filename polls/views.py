from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import Name

def test(request):
    if request.method == 'POST':
        return HttpResponse(json.dumps({'name': request.POST['your_name']}), content_type="application/json")
        # return render(request, "polls/test.html", {'name': request.POST['your_name']})
    return render(request, "polls/test.html")