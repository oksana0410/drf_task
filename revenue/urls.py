from django.urls import path
from . import views

urlpatterns = [
    path("revenue-statistics/", views.RevenueStatisticsView.as_view(), name="revenue-statistics"),
]
