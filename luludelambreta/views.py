from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'luludelambreta/index.html', context)

def detail(request, question_id):
    return HttpResponse(f'Essa é a pergunta de número {question_id}')

def results(request, question_id):
    question = Question(pk=question_id)
    return render(request, 'luludelambreta/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'luludelambreta/vote.html', {
            'question': question,
            'error_messange': "You did't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('luludelambreta:results', args=(question.id,)))

