from django.urls import include, path
from django.contrib import admin


api_urls = [
    path('todos/', include('todoapp.todos.urls')),
    path('', include('todoapp.users.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
