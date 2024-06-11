from django.shortcuts import render,redirect
from . import forms
from . import models
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        return super().form_valid(form)
    

class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'





    
    

