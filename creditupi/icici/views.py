from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from creditupi.icici.serializers import UpiSerializer, ErrorSerializer, CreditSerializer
from rest_framework.response import Response
from creditupi.icici.models import Upi, CreditUpi
from django.contrib.auth.models import User
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
        return Response(ErrorSerializer({"success": False, "message": "No data found"}).data)

class UpiExplorer(viewsets.ViewSet):
    # serializer_class = UpiSerializer

    def list(self, request):
        print("IN")
        queryset = Upi.objects.all().order_by('-pk')
        return Response(UpiSerializer(queryset, many=True).data)

    def retrieve(self, request, pk=None):
        if request.method == 'GET':
            print(request.data)
            if request.GET.get('type', '') == 'va':
                try:
                    queryset = UpiSerializer(Upi.objects.get(virtual_address=pk)).data
                except Upi.DoesNotExist:
                    queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
            else:
                try:
                    user = User.objects.get(username=pk)
                    queryset = Upi.objects.filter(author=user)
                    if (queryset.count() == 0):
                        queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
                    else:
                        queryset = UpiSerializer(queryset, many=True).data
                except User.DoesNotExist:
                    queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
        return Response(queryset)

    def create(self, request):
        if request.method == 'POST':
            try:
                u = Upi.objects.get(virtual_address=request.data.get('virtual-address'))
                if u is not None:
                    return Response(ErrorSerializer({"success": False, "message": "Record already exist"}).data)
            except Upi.DoesNotExist:
                try:
                    upi = Upi.objects.create(
                        mobile=request.data.get('mobile'),
                        device_id=request.data.get('device-id'),
                        seq_no=request.data.get('seq-no'),
                        channel_code=request.data.get('channel-code'),
                        virtual_address=request.data.get('virtual-address'),
                        author=User.objects.get(username=request.data.get('author'))
                    )
                    upi.save()
                    queryset = UpiSerializer(Upi.objects.get(pk=upi.id)).data
                except Exception as e:
                    print(e)
                    queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
                return Response(queryset)

class CreditExplorer(viewsets.ViewSet):

    def list(self, request):
        print("IN")
        queryset = CreditUpi.objects.all().order_by('-pk')
        return Response(CreditSerializer(queryset, many=True).data)

    def retrieve(self, request, pk=None):
        try:
            queryset = CreditSerializer(CreditUpi.objects.get(author=User.objects.get(username=pk))).data
        except CreditUpi.DoesNotExist:
            queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
            #handle case when user with that id does not exist
        return Response(queryset)

    def create(self, request):
        if request.method == 'POST':
            try:
                upi = CreditUpi.objects.create(
                    mobile=request.data.get('mobile'),
                    author=User.objects.get(username=request.data.get('author'))
                )
                upi.save()
                queryset = CreditSerializer(CreditUpi.objects.get(pk=upi.id)).data
            except Exception as e:
                print(e)
                queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
            return Response(queryset)

    def update(self, request, pk=None):
        if request.method == 'PUT':
            try:
                upi = CreditUpi.objects.get(pk=pk)
                upi.status = request.data.get('status', None)
                upi.save()
                queryset = CreditSerializer(upi).data
            except Exception as e:
                print(e)
                queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
            return Response(queryset)
