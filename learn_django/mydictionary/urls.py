from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import StartPage, read_from_file, add_to_file

urlpatterns = [
    path('', StartPage.as_view(), name='start_page'),
    path('home', StartPage.as_view(), name='start_page'),
    path('home/', StartPage.as_view(), name='start_page'),
    path('words_list', read_from_file, name='words_list'),
    path('words_list/', read_from_file, name='words_list'),
    path('add_word', add_to_file, name='add_word'),
    path('add_word/', add_to_file, name='add_word'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
