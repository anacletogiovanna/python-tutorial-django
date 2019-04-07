#Using to mapping the urls 
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),

    #ex: /polls/5/ - example url to get a question_id
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    #ex: /polls/id/result - example url to get a result 
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),

    #ex: polls/5/vote - example url to get a vote
    path('<int:question_id>/vote/', views.vote, name="vote"),
]