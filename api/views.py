import json

from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def api_home(request, *args, **kwargs):
    # request.body the data received from the request is initially a byte string of json data
    body = request.body
    print(body)
    data = {}
    try:
        data = json.loads(body)  # Converts jSon byte string to python dictionary
        print(data)
    except:
        pass
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    return JsonResponse(data)
