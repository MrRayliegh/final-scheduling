from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scheduling_system.urls')), 
<<<<<<< HEAD:django project/Scheduling_load/urls.py
]
=======
]
>>>>>>> 968c981 (Initial commit with Django project):Scheduling_load/urls.py
