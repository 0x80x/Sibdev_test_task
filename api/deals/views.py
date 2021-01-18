import csv
import datetime

from rest_framework import generics
from rest_framework.response import Response

from .serializer import *
from .models import *


class DealsListView(generics.ListCreateAPIView):
    serializer_class = DealsSerializer
    queryset = Deals.objects.all()

    def post(self, request, *args, **kwargs):
        mod = DealsSerializer()
        data = csv.DictReader(request.FILES['deals'].read().decode('utf-8').splitlines())

        try:
            for obj in data:
                mod.create(data=obj)
            response = {'Status': 'OK'}
        except Exception as e:
            response = {'Status': 'Error', 'Desc': f'{e} - в процессе обработки файла произошла ошибка'}

        return Response(response)

    # def get(self, request, *args, **kwargs):
    #     pass