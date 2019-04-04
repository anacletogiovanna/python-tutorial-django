#Using to mapping the urls 
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    #ex: /polls/5/ - example url to get a question_id
    path('<int:question_id>/', views.detail, name='detail'),

    #ex: /polls/id/result - example url to get a result 
    path('<int:question_id>/results/', views.results, name="results"),

    #ex: polls/5/vote - example url to get a vote
    path('<int:question_id>/vote/', views.vote, name="vote"),
]