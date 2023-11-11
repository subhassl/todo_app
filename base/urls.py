from django.urls import path
from .views import TaskList

from . import views

urlpatterns = [
    path('dummylist',views.dummyview,), 
    path('', TaskList.as_view(), name='tasks'),
]
