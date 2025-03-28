from django.shortcuts import render
from .models import Question, Choice
from .forms import QuizForm

def home(request):
    return render(request, 'quiz/home.html')

def quiz_view(request):
    questions = Question.objects.all()[:10]
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            for question in questions:
                selected_id = int(form.cleaned_data.get(f'question_{question.id}'))
                choice = Choice.objects.get(id=selected_id)
                if choice.is_correct:
                    score += 1
            return render(request, 'quiz/result.html', {'score': score})
    else:
        form = QuizForm(questions=questions)
    return render(request, 'quiz/quiz.html', {'form': form})
