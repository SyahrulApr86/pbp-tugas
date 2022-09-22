from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import ItemWatchList

# Create your views here.

def show_watchlist(request):
    data_itemwatchlist = ItemWatchList.objects.all()

    total_watched = ItemWatchList.objects.filter(watched='Yes').count()
    total_unwatched = ItemWatchList.objects.filter(watched='Not Yet').count()

    status = total_watched >= total_unwatched

    context = {
        'list_film': data_itemwatchlist,
        'nama': 'Syahrul Apriansyah',
        'student_id': '2106708311',
        'status': status
    }

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = ItemWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemWatchList.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = ItemWatchList.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ItemWatchList.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


