from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeamSerializer, PlayerSerializer, PlayerDetailSerializer, TeamDetailSerializer
from rest_framework.response import Response
from ..models import Team,Player

class TeamViewSet(viewsets.ViewSet):

    def get_queryset(self, request):
        queryset = Team.objects.all()
        country = request.query_params.get('country', None)
        if country:
            queryset = queryset.filter(country=country)
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = TeamDetailSerializer(queryset, many=True)
        return Response({
            'success': True,
            'result': serializer.data
        })

    def create(self, request):
        serializer = TeamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': True,
            'result': serializer.data
        })

    def delete(self, request ,pk=None):
        queryset = Team.objects.get(pk=pk)
        queryset.delete()
        return Response({
            'success': True,
            'result': {}
        })

    def update(self, request, pk=None):
        queryset = Team.objects.get(pk=pk)
        serializer = TeamSerializer(queryset,data=request.data,partial=True)
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
        queryset = Team.objects.get(pk=pk)
        serializer = TeamDetailSerializer(queryset)
        return Response({
            'success': True,
            'result': serializer.data
        })
        
class PlayerViewSet(viewsets.ViewSet):

    def get_queryset(self, request):
        queryset = Player.objects.all()
        name = request.query_params.get('name', None)
        category = request.query_params.get('category', None)
        if name:
            queryset = queryset.filter(name=name)
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = PlayerDetailSerializer(queryset, many=True)
        return Response({
            'success': True,
            'result': serializer.data
        })

    def create(self, request):
        serializer = PlayerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': True,
            'result': serializer.data
        })

    def delete(self, request ,pk=None):
        queryset = Player.objects.get(pk=pk)
        queryset.delete()
        return Response({
            'success': True,
            'result': {}
        })

    def update(self, request, pk=None):
        queryset = Player.objects.get(pk=pk)
        serializer = PlayerSerializer(queryset,data=request.data,partial=True)
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
        queryset = Player.objects.get(pk=pk)
        serializer = PlayerDetailSerializer(queryset)
        return Response({
            'success': True,
            'result': serializer.data
        })
        