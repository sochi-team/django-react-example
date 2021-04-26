from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView): #oтображать список объектов(ListView)
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]#Question.objects.filter(pub_date__lte=timezone.now())возвращает набор запросов, содержащий Questions, значение которого pub_dateменьше или равно - то есть раньше или равно - timezone.now.

class DetailView(generic.DetailView): #oтображать страницу сведений для опр типа объекта (DetailView)
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def index(request):
    #Отображает 5 вопросов, разделяя запятыми,в соответствии с датой
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',{'question':question})


def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #возвращает идентификатор выбранного варианта в виде строки
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"You didnt select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

