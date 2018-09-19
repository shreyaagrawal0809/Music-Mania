from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('music.urls')),
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('login/', include('music.urls')),
    path('home/', include('music.urls')),
    path('(?P<pk>[0-9]+)/favorite/', include('music.urls'))
]
