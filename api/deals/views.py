import csv
from collections import Counter

from rest_framework import generics
from rest_framework import status
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
            return Response({'Status': 'OK'}, status=status.HTTP_200_OK)
        except Exception as e:
            response = {'Status': 'Error', 'Desc': f'{e} - в процессе обработки файла произошла ошибка'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        data = {}
        # Получаем данные из бд и заполняем результат ответа
        for obj in Deals.objects.all():
            if obj.customer not in data:
                data[obj.customer] = {'spent_money': 0, 'gems': []}
            data[obj.customer]['spent_money'] += obj.total
            data[obj.customer]['gems'].append(obj.item)
        # Убираем дубликаты камней из покупок клиента
        for obj in data:
            data[obj]['gems'] = list(set(data[obj]['gems']))
        # Сортируем словарь с результатами для определения 5 топовых клиентов (нагуглил частично)
        data = {k: v for k, v in sorted(list(data.items()), key=lambda item: item[1]['spent_money'], reverse=True)}
        # Определяем топ 5 клиентов, кто поратил максимальное кол-во денег
        data = dict(list(data.items())[:5])
        # Формируем общий список камней которые купленны всеми топ5 клиентами
        # Далее мы подсчитываем число повторений камней что бы определить какие камни купили более 1 клиента
        gems_count = Counter(list([gem for lst in [g['gems'] for _, g in data.items()] for gem in lst]))
        # Копируем основной список для работы с ним и очищаем его
        data_tmp = data.copy()
        data.clear()
        # Тут я заполняю основной список по новой формируя то что требовалось
        for obj, info in data_tmp.items():
            data[obj] = {'spent_money': info['spent_money'], 'gems': []}
            for gem in info['gems']:
                if gems_count[gem] > 1:
                    data[obj]['gems'].append(gem)

        response = {'response': data}
        return Response(response, status=status.HTTP_200_OK)
