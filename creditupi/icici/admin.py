from django.contrib import admin
from creditupi.icici.models import Upi, CreditUpi, Users, Beneficiary, Transactions

# Register your models here.
admin.site.register(Upi)
admin.site.register(CreditUpi)
admin.site.register(Users)
admin.site.register(Beneficiary)
admin.site.register(Transactions)