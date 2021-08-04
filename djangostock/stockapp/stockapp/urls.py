from django.contrib import admin
from django.urls import path, include
from quote import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quote.urls')),
]
