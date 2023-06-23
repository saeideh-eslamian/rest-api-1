from django.urls import path
from . import views

urlpatterns = [
    path("",views.articel_list,name='articel'),
    path("<int:id>/",views.detail_articel,name='detail'),
]
