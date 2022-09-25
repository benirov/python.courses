
from django.template import Template, Context
from django.http import HttpResponse
import requests

def dashboard(request):

    dasboard = open("/home/zoomdevelopment/Documentos/workspace/courses/python/django/curso1/theme/templates/dashboard.html") 

    plt_dasboard =  Template(dasboard.read())

    dasboard.close()

    response = requests.get('https://text-view-miracles-api.onrender.com/api/textviews/1');

    dataInfo = response.json()
    ctx = Context({'textview' : dataInfo["textview"]})

    doc_dasboard = plt_dasboard.render(ctx)

    return HttpResponse(doc_dasboard)

def chaomundo(request):

    return HttpResponse("¡ Chao Mundo !")