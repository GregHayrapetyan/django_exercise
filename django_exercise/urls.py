"""django_exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from app.views import AuthorsView, AlbumsView, SongView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



api_info = openapi.Info(
    title="Django Exercise API",
    default_version="v1",
    description="API documentation for Django Exercise App",
)
schema_view = get_schema_view(
    api_info,
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs"),
    path("authors/", AuthorsView.as_view(), name="authors"),
    path("albums/", AlbumsView.as_view(), name="albums"),
    path("songs/", SongView.as_view(), name="songs"),
]
