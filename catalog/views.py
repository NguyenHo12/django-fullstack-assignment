from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Catalog app!")
def index(request):
    return render(request, 'catalog/index.html')