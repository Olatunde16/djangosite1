from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("pygo/", include("pygo.urls")),
    path("admin/", admin.site.urls),
]
