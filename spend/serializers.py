from rest_framework import serializers

from spend.models import SpendStatistic


class SpendStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = ("name", "date", "spend", "impressions", "clicks", "conversion")
