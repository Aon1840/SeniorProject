from django.http import HttpResponse, JsonResponse
from django.viewa.decorators.csrf import csrf_exampt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from CarPositions.models import CarPosition
from CarPositions.serializers import CarPositionSerializer

# # Create your views here.
# @csrf_exampt
# def get
