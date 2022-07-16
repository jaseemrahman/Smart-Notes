from django.shortcuts import render
from .models import Note
from django.http import Http404, HttpResponse, HttpResponseRedirect 
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from .forms import NoteForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#for forms
class NoteCreateView(LoginRequiredMixin,CreateView):
    model=Note
    success_url="/notes"
    form_class=NoteForm
    template_name='notes/notes_new.html'
    login_url='/admin'

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
     
#class based view -feature of django,we can avoid quries
class Notelistview(LoginRequiredMixin,ListView):
    model=Note
    context_object_name='notes'
    template_name='notes/notes_list.html'
    login_url='/admin'

    def queryset(self):
        return self.request.user.notes.all()

#detailview
class Notedetailview(DeleteView):
    model=Note
    context_object_name='note'
    template_name='notes/notes_detail.html'    
 

#delete
class NoteDeleteView(DeleteView):
    model=Note
    success_url="/notes"
    context_object_name='note'
    template_name='notes/notes_delete.html'

#update
class NoteUpdateView(UpdateView):
    model=Note
    success_url="/notes"
    form_class=NoteForm
    template_name ='notes/notes_edit.html'    