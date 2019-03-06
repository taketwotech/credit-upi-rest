from django.db import models
from django.utils import timezone
from django.conf import settings
from datetime import datetime, timedelta
from random import randint
from django.contrib.auth.models import User

def get_default_my_date():
    print(datetime.now().strftime('%s'))
    return datetime.now().timestamp()

def random_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def generate_limit():
    print(randint(5,10))
    return randint(5,10)*1000

class Upi(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    mobile = models.CharField(max_length=10)
    device_id = models.CharField(max_length=15)
    seq_no =  models.CharField(max_length=50)
    channel_code = models.CharField(max_length=10)
    virtual_address = models.CharField(max_length=10)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.virtual_address

class CreditUpi(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    account_no = models.IntegerField(default=get_default_my_date)
    created_date =  models.DateTimeField(default=timezone.now)
    mobile = models.IntegerField(unique=True)
    pin = models.IntegerField(default=random_number(4))
    status = models.CharField(max_length=1, default='P')
    limit = models.IntegerField(default=generate_limit())
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.account_no)
        
class Transactions(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    credit_upi_id = models.ForeignKey(CreditUpi, on_delete=models.CASCADE)
    trans_date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField() 
    status = models.CharField(max_length=1)  
    trans_key = models.CharField(max_length=100)

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
