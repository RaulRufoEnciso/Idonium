from django.shortcuts import render, redirect, get_object_or_404
from .models import Test, Question, Result, UserTestresult
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if request.method == 'POST':
        # Procesar respuestas, calcular el puntaje y guardar el resultado
        score = 0  # Aquí va la lógica para calcular el puntaje
        result = Result(user=request.user, test=test, score=score, completed_at=timezone.now())
        result.save()
        return redirect('profile')  # Redirige al perfil del usuario o a una página de resultados
    return render(request, 'take_test.html', {'test': test})

@login_required
def profile(request):
    results = Result.objects.filter(user=request.user)
    return render(request, 'profile.html', {'results': results})
@login_required
def user_dashboard(request):
    tests = Test.objects.all()
    return render(request, 'templates/user_dashboard.html', {'tests': tests})
@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, id = test_id)
    return render(request, 'templates/take_test.html', {'test': test})
@login_required
def user_profile(request):
    user_results = UserTestresult.objects.filter(user=request.user)
    return render(request, 'templates/user_profile.html', {'results': user_results})
@login_required
def evaluation_history(request):
    user_results = UserTestresult.objects.filter(user=request.user).order_by('-completed_at')
    return render(request, 'templates/evaluation_history.html', {'results': user_results})
@login_required
def compare_results(request):
    user_results = UserTestresult.objects.filter(user=request.user).order_by('-completed_at')
    # Aquí podríamos procesar datos para gráficos comparativos, por ejemplo, usando Matplotlib o Plotly
    return render(request, 'templates/compare_results.html', {'results': user_results})