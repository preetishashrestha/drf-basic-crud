from django.urls import path
from .views import TestApiView

urlpatterns = [
    path("test",TestApiView.as_view()),
    path("test/<id>",TestApiView.as_view())
]
