from django.urls import path
from .views import DataProcessingView

urlpatterns = [
    path('process/', DataProcessingView.as_view(), name='process'),
]
