
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100)
    TYPE_CHOICES = [
        ('pyschometric', 'Psicotécnico'),
        ('knowledge', 'Conocimiento'),
        ('skills', 'Habilidades')
    ]
    test_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    duration = models.PositiveIntegerField() #en minutos
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)

    ##ratio pregunta, boleean correcto o no , boleean si esta respondida o no, puntuacion
    QUESTION_TYPE_CHOICES = [
        ('multiple_choice', 'Opción múltiple'),
        ('true_false', 'Verdadero/Falso'),
        ('essay', 'Desarrollo')
    ]
    question_type = models.CharField(max_length=20, choices = QUESTION_TYPE_CHOICES)
    def __str__(self):
        return f"{self.text} ({self.test.name})"

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.text} ({self.question.text})"

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)

class UserTestresult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    hard_skills_score = models.DecimalField(max_digits=5, decimal_places=2)
    soft_skills_score = models.DecimalField(max_digits=5, decimal_places=2)
    completed_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.test.name} ({self.completed_at})"
