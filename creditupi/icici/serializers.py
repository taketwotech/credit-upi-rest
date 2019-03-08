from rest_framework import serializers
from creditupi.icici.models import Upi
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

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
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    first_name = serializers.CharField(source = "author.first_name")
    last_name = serializers.CharField(source = "author.last_name")
    username = serializers.CharField(source = "author.username")


class ErrorSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    message = serializers.CharField()

class CreditSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    account_no = serializers.IntegerField()
    limit = serializers.IntegerField()
    created_date =  serializers.DateTimeField()
    mobile = serializers.IntegerField()
    pin = serializers.IntegerField()
    status = serializers.CharField()
    created = serializers.DateTimeField()
    modified = serializers.DateTimeField()

class TokenSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')

class BeneficiarySerializer(serializers.Serializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    first_name = serializers.CharField(source = "author.first_name")
    last_name = serializers.CharField(source = "author.last_name")
    vpa = serializers.PrimaryKeyRelatedField(read_only=True)
    virtual_address = serializers.CharField(source = "vpa.virtual_address")
