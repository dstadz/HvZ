from django.shortcuts import render
from django.http import HttPresponse
# Create your views here.


def index(request):
  return HttPresponse("Hello World! You're at the polls index.")