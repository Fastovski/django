from django.contrib import admin

from .models import Products, Supplier, ExpertVoted, ProductVote

# Register your models here.

admin.site.register(Products)
admin.site.register(Supplier)
admin.site.register(ExpertVoted)
admin.site.register(ProductVote)
