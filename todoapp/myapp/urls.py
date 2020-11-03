from django.urls import path
from todoapp.myapp.views import (
    MyModelDetailAPIView,
    MyModelListCreateAPIView,
    detail,
    results,
    vote,
)
from todoapp.myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', MyModelListCreateAPIView.as_view(), name="list"),
    path('<int:pk>/', MyModelDetailAPIView.as_view(), name="detail"),
    # ex: /polls/
    path('index', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
