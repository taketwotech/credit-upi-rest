from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from creditupi.icici.serializers import SuccessSerializer, RequestSerializer
from rest_framework.response import Response
import requests

class ApiExplorer(viewsets.ViewSet):
    def create(self, request):
        restUrl = settings.GLOBAL_SETTINGS['REST_URL']
        apliKey = settings.GLOBAL_SETTINGS['API_KEY']
        if request.method == 'POST':
            response = requests.post( restUrl+ request.data.get('targetPoint'), 
                headers={"content-type":"application/json", "apikey": apliKey },
                json = request.data.get('data')).json()
            return Response(response)
        return Response("No data to process")
