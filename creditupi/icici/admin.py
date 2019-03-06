from django.contrib import admin
from creditupi.icici.models import Upi, CreditUpi, Users

# Register your models here.
admin.site.register(Upi)
admin.site.register(CreditUpi)
admin.site.register(Users)
