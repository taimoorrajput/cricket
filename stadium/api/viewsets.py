from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StadiumSerializer, StadiumDetailSerializer
from tournament.api.serializers import MatchSerializer, MatchDetailedSerializer
from rest_framework.response import Response
from tournament.models import Match
from ..models import Stadium

class StadiumViewSet(viewsets.ViewSet):

    def get_queryset(self, request):
        queryset = Stadium.objects.all()
        name = request.query_params.get('name', None)
        country = request.query_params.get('country', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = StadiumDetailSerializer(queryset, many=True)
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
        serializer = StadiumDetailSerializer(queryset)
        return Response({
            'success': True,
            'result': serializer.data
        })
        