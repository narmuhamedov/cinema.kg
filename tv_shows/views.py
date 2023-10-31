from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic


#создание шоу
class CreateShowView(generic.CreateView):
    template_name = 'crud/create_film.html'
    form_class = forms.TvShowForm
    queryset = models.TvShow.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateShowView, self).form_valid(form=form)


# def createShowView(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.TvShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлен <a href="/"> На главную </a> ')
#     else:
#         form = forms.TvShowForm()
#
#     return render(request, 'crud/create_film.html', {'form': form})


#список для удаления шоу
class DeleteShowView(generic.ListView):
    template_name = 'crud/del_film_list.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()

#процесс удаления(кнопка)
class DropFilmView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/delete_list/'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=film_id)

# def deleteListView(request):
#     if request.method == 'GET':
#         show = models.TvShow.objects.all()
#         context = {
#             'show_key': show,
#         }
#         html_name = 'crud/del_film_list.html'
#         return render(request, html_name, context)
#
#

# def dropFilmView(request, id):
#     film_id = get_object_or_404(models.TvShow, id=id)
#     film_id.delete()
#     return HttpResponse('Успешно удален <a href="/"> На главную </a> ')
#



#Список на изменение фильмов
class UpdateShowView(generic.ListView):
    template_name = 'crud/update_film_list.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()

#Процесс изменения(кнопка)
class EditShowView(generic.UpdateView):
    template_name = 'crud/edit.html'
    form_class = forms.TvShowForm
    success_url = '/update_list/'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=film_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditShowView, self).form_valid(form=form)

# def updateListView(request):
#     if request.method == 'GET':
#         show = models.TvShow.objects.all()
#         context = {
#             'show_key': show,
#         }
#         html_name = 'crud/update_film_list.html'
#         return render(request, html_name, context)
#
# def editFilmView(request, id):
#     film_id = get_object_or_404(models.TvShow, id=id)
#     if request.method == 'POST':
#         form = forms.TvShowForm(instance=film_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно изменен <a href="/"> На главную </a> ')
#     else:
#         form = forms.TvShowForm(instance=film_id)
#     context = {
#         'film_key':film_id,
#         'form':form,
#     }
#     return render(request, 'crud/edit.html', context)
#
#

#
#

#Главная страница

class TvShowListView(generic.ListView):
    template_name = 'tvshow/tvshow.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()

# def tvShowListView(request):
#     if request.method == 'GET':
#         show = models.TvShow.objects.all()
#         context = {
#             'show_key': show,
#         }
#         html_name = 'tvshow/tvshow.html'
#         return render(request, html_name, context)

# Получение ID
class TvShowDetailView(generic.DetailView):
    template_name = 'tvshow/tvshow_detail.html'
    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=film_id)

# def tvShowDetailView(request, id):
#     show_id = get_object_or_404(models.TvShow, id=id)
#     context = {
#         'show_id_key': show_id,
#     }
#     html_detail_name = 'tvshow/tvshow_detail.html'
#     return render(request, html_detail_name, context)
