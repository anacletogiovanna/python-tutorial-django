#Setting the view of application

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lasted_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):


    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())



def index(request):
    lasted_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lasted_question_list': lasted_question_list,}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})
    
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


