from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from getnama.models import HitungNama
from getnama.serializers import TotalSerializer
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
db = client['teknofestdb']
listorang = db.listorangcoba


# Create your views here.
@api_view(['GET'])
def total_detail(request, nama,format=None):
    try:
        namanya = str(nama).upper()
        totalnya = listorang.find({"$text": {"$search": namanya}}).count()
        totalnamalakinya = listorang.find({"$text": {"$search": namanya},'kelamin' : 'L'}).count()
        totalnamaperempuannya = listorang.find({"$text": {"$search": namanya},'kelamin' : 'P'}).count()
        total = HitungNama(nama=namanya,total = totalnya,totalnamalaki = totalnamalakinya,totalnamaperempuan = totalnamaperempuannya)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TotalSerializer(total)
        return Response(serializer.data)