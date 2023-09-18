from rest_framework import generics

from apps.tests.models import Test
from apps.tests.serializers import TestSerializer


class TestListAPIView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Test.objects.filter(course=pk)
