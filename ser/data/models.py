from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.o

class Data(models.Model):
  time = models.CharField(max_length=100)
  ident = models.CharField(max_length=100)
  value = models.CharField(max_length=100)


class Show(admin.ModelAdmin):
  list_display=('time','ident','value')
  search_fields = ['time',]


admin.site.register(Data,Show)
