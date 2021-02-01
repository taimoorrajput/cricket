from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StadiumSerializer
from rest_framework.response import Response
from ..models import Stadium

class StadiumViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Stadium.objects.all()
        serializer = StadiumSerializer(queryset, many=True)
        return Response({
            'success': True,
            'result': serializer.data
        })

    def create(self, request):
        serializer = StadiumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': True,
            'result': serializer.data
        })

    def delete(self, request ,pk=None):
        queryset = Stadium.objects.get(pk=pk)
        queryset.delete()
        return Response({
            'success': True,
            'result': {}
        })

    def update(self, request, pk=None):
        queryset = Stadium.objects.get(pk=pk)
        serializer = StadiumSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'success': True,
            'result': serializer.data
        })
        return Response({
            'success': False,
            'result': serializer.error
            })

    def retrieve(self, request, pk=None):
        queryset = Stadium.objects.get(pk=pk)
        serializer = StadiumSerializer(queryset)
        return Response({
            'success': True,
            'result': serializer.data
        })
        