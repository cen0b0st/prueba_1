from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    doc_externo = open("G:/software PAI/front/Front/frontweb/templates/frontweb/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    contexto = datetime.today().strftime('%d-%m-%Y')
    ctx = Context({"fecha":contexto})
    documento = plt.render(ctx)
    return HttpResponse(documento)