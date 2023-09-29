from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from spend.models import SpendStatistic
from spend.serializers import SpendStatisticSerializer


class SpendStatisticView(APIView):
    def get(self, request):
        queryset = SpendStatistic.objects.values("date", "name").annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversion=Sum("conversion")
        ).prefetch_related("revenuestatistics_set")

        serializer = SpendStatisticSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
