from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

def propertyList(request):
    return  render(request, 'main/properties.html')