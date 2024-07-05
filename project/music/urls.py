from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name="music"
urlpatterns = [
    path('',views.singer_list_create),
    path('<int:singer_id>',views.singer_detail_update_delete),
    path('<int:singer_id>/song',views.song_list_create),
    path('<int:singer_id>/song/<int:song_id>',views.song_detail_update_delete),
    path('tags/<str:tag_name>', views.find_tag),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)