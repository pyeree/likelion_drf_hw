from django.urls import path
from .views import *
from . import views

app_name="music"
urlpatterns = [
    path('',views.singer_list_create),
    path('singer/<int:singer_id>',views.singer_detail_update_delete),
    path('<int:singer_id>/song',views.song_list_create),
    path('song/<int:song_id>',views.song_detail_update_delete),
]