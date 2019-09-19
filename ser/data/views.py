from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json

from . import models

# Create your views here.
def receive(request): 
  t = request.GET.get('time')
  i = request.GET.get('id')
  v = request.GET.get('value')
  d = models.Data(time=t,ident=i,value=v)
  d.save()

  return HttpResponse(t)

def send(request):
  time1 = request.GET.get('time1')
  time2 = request.GET.get('time2')
  type1 = request.GET.get('type')
  data = models.Data.objects.filter(time__gte=time1)
  data = data.filter(time__lte=time2)
  l = []
  for i in range(0,5):
	  if type1[i] == '1':
		  l.append(data.filter(ident=i))
  s=""
  for data in l:
	  for d in data:
		  s+=d.time
		  s+="_"
		  s+=d.ident
		  s+="_"
		  s+=d.value
		  s+="\n"
  s+="aaa"

  return HttpResponse(s)
