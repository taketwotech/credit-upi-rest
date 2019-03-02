from rest_framework import serializers

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
