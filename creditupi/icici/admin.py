from django.contrib import admin
from creditupi.icici.models import Upi, CreditUpi, Users, Beneficiary

# Register your models here.
admin.site.register(Upi)
admin.site.register(CreditUpi)
admin.site.register(Users)
admin.site.register(Beneficiary)
