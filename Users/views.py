# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Users.models import User
from Users.serializers import UserSerializer
import json
# Create your views here.

@csrf_exempt
def getAllUser(request):
    #method for list all users

    if request == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return JsonResponse(serializer.data,self=False)

    elif request == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.erroes, statuss=400)


@csrf_exempt
def getUserDetail(request,pk):
    #method for see user detail

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user, many=True)

        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

def ShowAllUser(request):
    ul = User.objects.filter()
    Alluser = []
    for us in ul :
        Alluser.append({
            "user_id" : us.user_id,
            "username" : us.username,
            "password" : us.password,
            "name" : us.name,
            "surname" : us.surname,
            "tel" : us.tel,
            "email" : us.email,
            "register_date" : us.register_date
        })

        context = {
            'obj' : Alluser
        }

    return HttpResponse(json.dumps(context),content_type="application/json")





