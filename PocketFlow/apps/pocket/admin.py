from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Account, Transaction

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass

@admin.register(Account)
class AccountAdmin(ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display=["transaction_type", "amount", "account", "category"]