from django.urls import path
from .import views
urlpatterns = [
    path('notes',views.Notelistview.as_view(),name='notes.list'),
    path('notes/<int:pk>',views.Notedetailview.as_view(),name='notes.detail'),
    path('notes/<int:pk>/edit',views.NoteUpdateView.as_view(),name='notes.update'),
    path('notes/<int:pk>/delete',views.NoteDeleteView.as_view(),name='notes.delete'),
    path('notes/new',views.NoteCreateView.as_view(),name='notes.new'),
 
]
