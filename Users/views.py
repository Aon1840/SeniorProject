# from django.shortcuts import render
from django.http import HttpResponse, JSONResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRender
from rest_framework.parsers import JSONParser
from Users.models import User
from Users.serializers import UserSerializer
# Create your views here.

@csrf_exempt
def getAllUser(request): #method for list all users
    if request == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)

        return JSONResponse(serializer.data,self=False)

    elif request == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.erroes, statuss=400)


@csrf_exempt
def getUserDetail(request,pk): #method for see user detail
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user, many=True)

        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)





