from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Link 
from .serializers import LinkSerializer


class ResolverView(APIView):
    def get(self, request: Request, alias: str):
        try:
            link = Link.objects.get(alias=alias)
        except Link.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LinkSerializer(link)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShortenerView(APIView):
    def post(self, request: Request, *args, **kwargs):
        data = {
            'url': request.data.get('url'), 
            'alias': request.data.get('alias'),
        }
        serializer = LinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
