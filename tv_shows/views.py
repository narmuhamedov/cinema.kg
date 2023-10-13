from django.shortcuts import render, get_object_or_404
from . import models


def tvShowListView(request):
    show = models.TvShow.objects.all()
    context = {
        'show_key': show,
    }
    html_name = 'tvshow/tvshow.html'
    return render(request, html_name, context)


def tvShowDetailView(request, id):
    show_id = get_object_or_404(models.TvShow, id=id)
    context = {
        'show_id_key': show_id,
    }
    html_detail_name = 'tvshow/tvshow_detail.html'
    return render(request, html_detail_name, context)
