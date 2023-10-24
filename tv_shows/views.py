from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse

def createShowView(request):
    method = request.method
    if method == 'POST':
        form = forms.TvShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлен <a href="/"> На главную </a> ')
    else:
        form = forms.TvShowForm()

    return render(request, 'crud/create_film.html', {'form': form})


def deleteListView(request):
    if request.method == 'GET':
        show = models.TvShow.objects.all()
        context = {
            'show_key': show,
        }
        html_name = 'crud/del_film_list.html'
        return render(request, html_name, context)


def updateListView(request):
    if request.method == 'GET':
        show = models.TvShow.objects.all()
        context = {
            'show_key': show,
        }
        html_name = 'crud/update_film_list.html'
        return render(request, html_name, context)

def editFilmView(request, id):
    film_id = get_object_or_404(models.TvShow, id=id)
    if request.method == 'POST':
        form = forms.TvShowForm(instance=film_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно изменен <a href="/"> На главную </a> ')
    else:
        form = forms.TvShowForm(instance=film_id)
    context = {
        'film_key':film_id,
        'form':form,
    }
    return render(request, 'crud/edit.html', context)


def dropFilmView(request, id):
    film_id = get_object_or_404(models.TvShow, id=id)
    film_id.delete()
    return HttpResponse('Успешно удален <a href="/"> На главную </a> ')



def tvShowListView(request):
    if request.method == 'GET':
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
