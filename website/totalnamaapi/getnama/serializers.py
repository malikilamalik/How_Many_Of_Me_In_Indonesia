from rest_framework import serializers
from getnama.models import HitungNama

class TotalSerializer(serializers.Serializer):
    nama = serializers.CharField(required=True,max_length=100)
    total = serializers.IntegerField(required=True)
    totalnamalaki = serializers.IntegerField(required=True)
    totalnamaperempuan = serializers.IntegerField(required=True)