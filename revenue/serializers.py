from rest_framework import serializers

from revenue.models import RevenueStatistics
from spend.serializers import SpendStatisticSerializer


class RevenueStatisticSerializer(serializers.ModelSerializer):
    spend = SpendStatisticSerializer()

    class Meta:
        model = RevenueStatistics
        fields = ("name", "date", "revenue", "spend")
