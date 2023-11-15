from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Tag, Question, answer, user
from django.shortcuts import render, HttpResponse, get_object_or_404
# Create your views here.
ANSWER = [
    {
        'id': i,
        'text': f'answer{i}'
    } for i in range(60)
]


def paginate(objects, page, per_page=20):
    paginator = Paginator(objects, per_page)
    return paginator.get_page(page)

def index(request):
    page = request.GET.get('page', 1)
    questionsMassiv = Question.objects.new_questions()
    return render(request, 'index.html', {
        'questions': paginate(questionsMassiv, page),
        'page': page,
    })


def question(request, question_id):
    question_components = Question.objects.get(pk=question_id)
    answerMassiv = answer.objects.hot_answers()

    page = request.GET.get('page', 1)
    return render(request, 'question.html', {'question': question_components, 'questions': paginate(answerMassiv, page, 30)})


def hot(request):
    questions = Question.objects.hot_questions()
    page = request.GET.get('page', 1)

    return render(request, 'hot.html', {
        'questions': paginate(questions, page),
        'page': page,
    })


def Ask(request):
    return render(request, 'Ask.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def settings(request):
    return render(request, 'settings.html')

def tag(request, text=None):
    tag =get_object_or_404(Tag, text=text)
    questions = tag.question_set.new_questions()
    page = request.GET.get('page', 1)
    return render(request, 'tag.html', {
        'tag': tag,
        'questions': paginate(questions, page),
        'page': page
    })