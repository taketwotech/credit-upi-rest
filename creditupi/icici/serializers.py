from rest_framework import serializers
from creditupi.icici.models import Upi

class RequestSerializer(serializers.Serializer):
    targetPoint = serializers.CharField()
    data = serializers.CharField()

class SuccessSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    response = serializers.IntegerField()
    message = serializers.CharField()
    BankRRN = serializers.CharField()
    UpiTranlogId = serializers.CharField()
    UserProfile = serializers.CharField()
    SeqNo = serializers.CharField()
    MobileAppData= serializers.CharField()

class UpiSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    mobile = serializers.CharField()
    device_id = serializers.CharField()
    seq_no =  serializers.CharField()
    channel_code = serializers.CharField()
    virtual_address = serializers.CharField()
    created = serializers.DateTimeField()
    modified = serializers.DateTimeField()

class ErrorSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    message = serializers.CharField()

class CreditSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    account_no = serializers.IntegerField()
    created_date =  serializers.DateTimeField()
    mobile = serializers.IntegerField()
    pin = serializers.IntegerField()
    status = serializers.CharField()
    created = serializers.DateTimeField()
    modified = serializers.DateTimeField()