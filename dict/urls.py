from django.contrib import admin
from django.urls import path, include

from dict.views import home_page, words_list, CreateWord

urlpatterns = [
    path('', home_page, name='homepage'),
    path('words/', words_list, name='words-list'),
    path('word-create/', CreateWord.as_view(), name='word_create'),
]