from django.contrib import admin  # Import admin module
from django.urls import path, include  # Import path and include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the app's URLs
]
