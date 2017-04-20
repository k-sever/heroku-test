from django.http import HttpResponse
from django.shortcuts import render

from .models import Name

def test(request):
    if request.method == 'POST':
        return render(request, "polls/test.html", {'name': request.POST['your_name']})
    return render(request, "polls/test.html")