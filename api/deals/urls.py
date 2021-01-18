from django.urls import path
from .views import *


urlpatterns = [
    path('', DealsListView.as_view())
]