from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Voyage,Excursion,Destination
# Create your views here.
from django.template import loader
from .formulaire import VoyageForm


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request=request))

def excursion(request):
    excursion = Excursion.objects.all()
    #formated_excursion = ["<li>{}</li>".format(dest.nom) for dest in excursion]
    #message = """<ul>{}</ul>""".format("\n".join(formated_excursion))
    #return HttpResponse(message)
    return render(request,'excursion.html',{'excursion':excursion})
    #template = loader.get_template('excursion.html')
    #return HttpResponse(template.render(request=request))

def voyage(request):
    voyage = Voyage.objects.all()
    #formated_voyage = ["<li>{}</li>".format(dest.nom) for dest in voyage]
    #message = """<ul>{}</ul>""".format("\n".join(formated_voyage))
    return render(request,'voyage.html',{'voyage':voyage})
    #return HttpResponse(message)
    #template = loader.get_template('voyage.html')
    #return HttpResponse(template.render(request=request))

def destination(request):
    destination = Destination.objects.filter()
    #formated_destination = ["<li>{}</li>".format(dest.pays)for dest in destination]
    #message = """<ul>{}</ul>""".format("\n".join(formated_destination))
    return render(request,'destination.html',{'destination':destination})
    #return HttpResponse(message)
    #template = loader.get_template('destination.html')
    #return HttpResponse(template.render(request=request))

def voyage_detail(request):
    voyage_detail = Excursion.objects.filter()
    for x in voyage_detail:
        if request.method == 'POST':
            name = request.POST.get('nom')
        if x.nom == name:
            voyage_detail = x.excursion.filter()
            return render(request,'voyage_detail.html',{'voyage_detail':voyage_detail})

def voyage_dest(request):
    voyage_dest = Destination.objects.filter()
    for x in voyage_dest:
        if request.method == 'POST':
            name = request.POST.get('nom')
            if x.pays == name:
                voyage_dest = x.voyage.filter()
                return render(request,'voyage_dest.html',{'voyage_dest':voyage_dest})

def ajout_voyage(request):
    if request.method == "POST":
        form = VoyageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/destination')
    else:
        form = VoyageForm()

    return render(request,'ajout_voyage.html',{'form':form})