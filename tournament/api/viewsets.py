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
            'data list': serializer.data
        })

    def create(self, request):
        serializer = TournamentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'created data': serializer.data
        })

    def delete(self, request ,pk=None):
        id = pk
        queryset = Tournament.objects.get(pk=id)
        queryset.delete()
        return Response({
            'msg':'data deleted'
        })

    def update(self, request, pk=None):
        id = pk
        queryset = Tournament.objects.get(pk=id)
        serializer = TournamentSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'updated data': serializer.data
            })
        return Response(serializer.error)

    def retrieve(self, request, pk=None):
        id = pk
        queryset = Tournament.objects.get(pk=id)
        serializer = TournamentSerializer(queryset)
        return Response({
            'retrived data':serializer.data
        })
        
class MatchViewSet(viewsets.ViewSet):
    queryset = Match.objects.all()

    def list(self, request):
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response({
            'data list': serializer.data
        })

    def create(self, request):
        serializer = MatchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'created data': serializer.data
        })

    def delete(self, request ,pk=None):
        id = pk
        queryset = Match.objects.get(pk=id)
        queryset.delete()
        return Response({
            'msg':'data deleted'
        })

    def update(self, request, pk=None):
        id = pk
        queryset = Match.objects.get(pk=id)
        serializer = MatchSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
            #    'msg':'partial data is updated',
                'updated data':serializer.data
            })
        return Response(serializer.error)

    def retrieve(self, request, pk=None):
        id = pk
        queryset = Match.objects.get(pk=id)
        serializer = MatchSerializer(queryset)
        return Response({
            'retrived data':serializer.data
        })
        