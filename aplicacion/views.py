from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"aplicacion/index.html")

def saludo(request):
    return render(request,"aplicacion/saludo.html")

def extra(request):
    return render(request,"aplicacion/extra.html")