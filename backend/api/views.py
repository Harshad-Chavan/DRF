from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body  # --> this is a byte string of json data
    print(body)
    print(request.GET)
    data = {}
    try:
        data = json.loads(body)  # converts string of json datra into python dictionary
    except:
        pass
    data["params"] = dict(request.GET)
    data["headers"] = dict(
        request.headers
    )  # httpheader cannot be directly seriablaized convert them into dicitonary first
    data["content_type"] = request.content_type
    print(data.keys())
    return JsonResponse(data)
