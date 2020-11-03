from django.urls import include, path
from django.contrib import admin


api_urls = [
    path('todos/', include('todoapp.todos.urls')),
    path('users/', include('todoapp.users.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(api_urls)),
    path('myapp/', include('todoapp.myapp.urls')),
]
