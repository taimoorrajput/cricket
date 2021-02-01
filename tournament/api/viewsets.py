from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TournamentSerializer,MatchSerializer
from rest_framework.response import Response
from ..models import Tournament,Match

class TournamentViewSet(viewsets.ViewSet):
    queryset = Tournament.objects.all()

    def list(self, request):
        queryset = Tournament.objects.all()
        serializer = TournamentSerializer(queryset, many=True)
        return Response({
            'success': True,
            'result': serializer.data
        })

    def create(self, request):
        serializer = TournamentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': True,
            'result': serializer.data
        })

    def delete(self, request ,pk=None):
        queryset = Tournament.objects.get(pk=pk)
        queryset.delete()
        return Response({
            'success': True,
            'result': serializer.data
        })

    def update(self, request, pk=None):
        queryset = Tournament.objects.get(pk=pk)
        serializer = TournamentSerializer(queryset,data=request.data,partial=True)
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
        queryset = Tournament.objects.get(pk=pk)
        serializer = TournamentSerializer(queryset)
        return Response({
            'success': True,
            'result': serializer.data
        })
        
class MatchViewSet(viewsets.ViewSet):
    queryset = Match.objects.all()

    def list(self, request):
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response({
            'success': True,
            'result': serializer.data
        })

    def create(self, request):
        serializer = MatchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': True,
            'result': serializer.data
        })

    def delete(self, request ,pk=None):
        id = pk
        queryset = Match.objects.get(pk=id)
        queryset.delete()
        return Response({
            'success': True,
            'result': {}
        })

    def update(self, request, pk=None):
        queryset = Match.objects.get(pk=pk)
        serializer = MatchSerializer(queryset,data=request.data,partial=True)
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
        queryset = Match.objects.get(pk=pk)
        serializer = MatchSerializer(queryset)
        return Response({
            'success': True,
            'result': serializer.data
        })
        