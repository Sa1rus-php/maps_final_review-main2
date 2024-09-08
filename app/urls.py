from django.urls import path

from .views import IndexView, DeleteView

urlpatterns = [
    path("", IndexView.as_view()),
    path("delete_all/", DeleteView.as_view())
]

