from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

def propertyList(request):
    return  render(request, 'main/properties.html')

def property(request):
    return  render(request, 'main/properties-detail.html')

def owners(request):
    return  render(request, 'main/landowner.html')

def contact(request):
    return  render(request, 'main/contact.html')

def error_404_view(request, exception):
    return render(request,'404.html')