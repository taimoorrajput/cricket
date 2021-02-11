from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TournamentSerializer, MatchSerializer, MatchDetailedSerializer, TournamentDetailSerializer
from rest_framework.response import Response
from ..models import Tournament,Match
from stadium.models import Stadium

class TournamentViewSet(viewsets.ViewSet):

    def get_queryset(self, request):
        queryset = Tournament.objects.all()
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = TournamentDetailSerializer(queryset, many=True)
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
        serializer = TournamentDetailSerializer(queryset)
        return Response({
            'success': True,
            'result': serializer.data
        })
        
class MatchViewSet(viewsets.ViewSet):

    def get_queryset(self, request):
        queryset = Match.objects.all()
        toss = request.query_params.get('toss', None)
        name = request.query_params.get('name',None)
        if toss is not None:
            queryset = queryset.filter(toss=toss)
        if name is not None:
            queryset = queryset.filter(tournament__name=name)
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = MatchDetailedSerializer(queryset, many=True)
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
        queryset = Match.objects.get(pk=pk)
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
        serializer = MatchDetailedSerializer(queryset)
        return Response({
            'success': True,
            'result': serializer.data
        })
        