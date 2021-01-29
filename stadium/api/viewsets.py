from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StadiumSerializer
from rest_framework.response import Response
from ..models import Stadium

class StadiumViewSet(viewsets.ViewSet):
    queryset = Stadium.objects.all()

    def list(self, request):
        queryset = Stadium.objects.all()
        serializer = StadiumSerializer(queryset, many=True)
        return Response({
            'data List': serializer.data
        })

    def create(self, request):
        serializer = StadiumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'created data': serializer.data
        })

    def delete(self, request ,pk=None):
        id = pk
        queryset = Stadium.objects.get(pk=id)
        queryset.delete()
        return Response({
            'msg':'data deleted'
        })

    def update(self, request, pk=None):
        id = pk
        queryset = Stadium.objects.get(pk=id)
        serializer = StadiumSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data updated': serializer.data
            })
        return Response(serializer.error)

    def retrieve(self, request, pk=None):
        id = pk
        queryset = Stadium.objects.get(pk=id)
        serializer = StadiumSerializer(queryset)
        return Response({
            'retrived data':serializer.data
        })
        