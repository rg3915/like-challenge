from myproject.core import views as v
from django.urls import path

urlpatterns = [
    path('', v.index, name='index'),
]
