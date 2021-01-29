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
            'data list': serializer.data
        })

    def create(self, request):
        serializer = TeamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'created data': serializer.data
        })

    def delete(self, request ,pk=None):
        id = pk
        queryset = Team.objects.get(pk=id)
        queryset.delete()
        return Response({
            'msg':'data deleted'
        })

    def update(self, request, pk=None):
        id = pk
        queryset = Team.objects.get(pk=id)
        serializer = TeamSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
#                'msg':'partial data is updated'
                'updated data': serializer.data
            })
        return Response(serializer.error)

    def retrieve(self, request, pk=None):
        id = pk
        queryset = Team.objects.get(pk=id)
        serializer = TeamSerializer(queryset)
        return Response({
            'retrived data':serializer.data
        })
        
class PlayerViewSet(viewsets.ViewSet):
    queryset = Player.objects.all()

    def list(self, request):
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
        return Response({
            'data list': serializer.data
        })

    def create(self, request):
        serializer = PlayerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'created data': serializer.data
        })

    def delete(self, request ,pk=None):
        id = pk
        queryset = Player.objects.get(pk=id)
        queryset.delete()
        return Response({
            'msg':'data deleted'
        })

    def update(self, request, pk=None):
        id = pk
        queryset = Player.objects.get(pk=id)
        serializer = PlayerSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
            #    'msg':'partial data is updated'
                'created data': serializer.data
            })
        return Response(serializer.error)

    def retrieve(self, request, pk=None):
        id = pk
        queryset = Player.objects.get(pk=id)
        serializer = PlayerSerializer(queryset)
        return Response({
            'retrived data':serializer.data
        })
        