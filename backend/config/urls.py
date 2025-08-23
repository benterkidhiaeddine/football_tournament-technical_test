from django.contrib import admin
from django.urls import path, include

from tournament import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    # Include other app URLs here
    path('tournament/', include(urls)),


]