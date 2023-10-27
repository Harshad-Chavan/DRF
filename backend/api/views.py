from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# def api_home(request, *args, **kwargs):
#     body = request.body  # --> this is a byte string of json data
#     print(body)
#     print(request.GET)
#     data = {}
#     try:
#         data = json.loads(body)  # converts string of json datra into python dictionary
#     except:
#         pass
#     data["params"] = dict(request.GET)
#     data["headers"] = dict(
#         request.headers
#     )  # httpheader cannot be directly seriablaized convert them into dicitonary first
#     data["content_type"] = request.content_type
#     print(data.keys())
#     return JsonResponse(data)

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price
        data = model_to_dict(model_data, fields=["id", "title", "price"])
    return Response(data)
