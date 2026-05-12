from rest_framework.routers import DefaultRouter
from .views import crudView
from django.urls import path,include
router=DefaultRouter()
router.register("view",crudView)
urlpatterns=[
        path("", include(router.urls))
]