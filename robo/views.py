from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Studenta
from .serializers import StudentaSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

@csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Studenta.objects.get(id=id)
#             serializer = StudentaSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
        
#         stu = Studenta.objects.all()
#         serializer = StudentaSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentaSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Crated'} 
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Studenta.objects.get(id=id)
#         serializer = StudentaSerializer(stu, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Updated'} 
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
        

#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Studenta.objects.get(id=id)
#         stu.delete()
#         res = {'msg': 'Data Deleted'} 
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')


@api_view(['GET', 'POST','PUT', 'DELETE'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'This is GET request'})
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'This is POST request', 'data': request.data})

    if request.method == 'PUT':
        print(request.data)
        return Response({'msg': 'This is PUT request', 'data': request.data})