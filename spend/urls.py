from django.urls import path
from . import views

urlpatterns = [
    path("spend-statistics/", views.SpendStatisticView.as_view(), name="spend-statistics"),
]
