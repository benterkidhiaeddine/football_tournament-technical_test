from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include other app URLs here
    path('tournament/', include("tournament.urls")),
    path('api/', include("api.urls"))


]