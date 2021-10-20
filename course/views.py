from django.http.response import HttpResponse, ResponseHeaders
from rest_framework import generics
from . import serializers
from . import models

class text_content(generics.CreateAPIView):
    queryset = models.text_content.objects.all()
    serializer_class = serializers.tcSerializers

class image_content(generics.CreateAPIView):
    queryset = models.img_content.objects.all()
    serializer_class = serializers.icSerializers
