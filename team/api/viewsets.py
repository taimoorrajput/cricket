from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeamSerializer,PlayerSerializer
from rest_framework.response import Response
from ..models import Team,Player

class TeamViewSet(viewsets.ViewSet):
    queryset = Team.objects.all()

    def list(self, request):
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset, many=True)
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
        serializer = TeamSerializer(queryset)
        return Response({
            'success': True,
            'result': serializer.data
        })
        
class PlayerViewSet(viewsets.ViewSet):
    queryset = Player.objects.all()

    def list(self, request):
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
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
        serializer = PlayerSerializer(queryset)
        return Response({
            'success': True,
            'result': serializer.data
        })
        