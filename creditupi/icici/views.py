from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from creditupi.icici.serializers import UpiSerializer, ErrorSerializer, \
        CreditSerializer, BeneficiarySerializer, TransactionSerializer
from rest_framework.response import Response
from creditupi.icici.models import Upi, CreditUpi, Users, Beneficiary, Transactions
from django.contrib.auth.models import User
import requests
from django.db.models import Sum

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
            if request.GET.get('type', '') == 'va':
                try:
                    u = Upi.objects.get(virtual_address=pk)
                    print(u.author)
                    queryset = UpiSerializer(u).data
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
        queryset = CreditUpi.objects.all().order_by('-pk')
        return Response(CreditSerializer(queryset, many=True).data)

    def retrieve(self, request, pk=None):
        try:
            cupi = CreditUpi.objects.get(author=User.objects.get(username=pk))
            trans = Transactions.objects.filter(author=User.objects.get(username=pk), credit_upi_id=cupi, trans_type='DB').aggregate(Sum('amount'))
            trans_credited = Transactions.objects.filter(author=User.objects.get(username=pk), credit_upi_id=cupi, trans_type='CR').aggregate(Sum('amount'))
            cupi.limit = cupi.limit
            cupi.used = 0 if (trans.get('amount__sum') == None) else trans.get('amount__sum')
            cupi.credited = 0 if (trans_credited.get('amount__sum') == None) else trans_credited.get('amount__sum')
            queryset = CreditSerializer(cupi).data
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
                if request.data.get('vpa') is not None:
                    upi.vpa = Upi.objects.get(virtual_address=request.data.get('vpa'))
                if request.data.get('status') is not None:
                    upi.status = request.data.get('status', None)
                upi.save()
                queryset = CreditSerializer(upi).data
            except Exception as e:
                print(e)
                queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
            return Response(queryset)

class BeneficiaryExplorer(viewsets.ViewSet):
    def list(self, request):
        queryset = Beneficiary.objects.all().order_by('-pk')
        return Response(BeneficiarySerializer(queryset, many=True).data)

    def create(self, request):
        if request.method == 'POST':
            try:
                beneficiary = Beneficiary.objects.create(
                    author=User.objects.get(username=request.data.get('author')),
                    vpa=Upi.objects.get(virtual_address=request.data.get('vpa'))
                )
                beneficiary.save()
                queryset = BeneficiarySerializer(Beneficiary.objects.get(pk=beneficiary.id)).data
            except Exception as e:
                print(e)
                queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
            return Response(queryset)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(username=pk)
            queryset = Beneficiary.objects.filter(author=user)
            if (queryset.count() == 0):
                queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
            else:
                queryset = BeneficiarySerializer(queryset, many=True).data
        except User.DoesNotExist:
            queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
        return Response(queryset)

class PaymentExplorer(viewsets.ViewSet):
    def create(self, request):
        if request.method == 'POST':
            try:
                author = User.objects.get(username=request.data.get('author'))
                payment = Transactions.objects.create(
                    author = author,
                    credit_upi_id = CreditUpi.objects.get(author=author),
                    amount = request.data.get('amount', 0),
                    status = 'A',
                    trans_type = request.data.get('trans_type', 'CR'),
                    description = request.data.get('description')
                )
                payment.save()
                queryset = ErrorSerializer({"success": True, "message": "No data found"}).data
            except Exception as e:
                print(e)
                queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
            return Response(queryset)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(username=pk)
            queryset = Transactions.objects.filter(author=user)
            if (queryset.count() == 0):
                queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
            else:
                queryset = TransactionSerializer(queryset, many=True).data
        except User.DoesNotExist:
            queryset = ErrorSerializer({"success": False, "message": "No data found"}).data
        return Response(queryset)
