from django.shortcuts import render

# Create your views here.
def index(request):
    render(request,'basic_app/index.html')

def other(request):
    render(request,'basic_app/other.html')

def relative_url(request):
    render(request,'basic_app/relative_url_templates.html')
