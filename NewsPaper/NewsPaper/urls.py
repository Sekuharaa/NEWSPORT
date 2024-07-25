from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('news.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')),
    path('accounts/', include('allauth.urls')),

]


