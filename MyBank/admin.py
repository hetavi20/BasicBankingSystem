from django.contrib import admin

from MyBank.models import customerDetail, transaction

# Register your models here.
admin.site.register(customerDetail)
admin.site.register(transaction)