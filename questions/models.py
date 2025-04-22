from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class QuestionType(models.Model):
    exam = models.ForeignKey('exams.Exam', on_delete=models.CASCADE, related_name='question_types')
    position = models.PositiveIntegerField()
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'question_types'
        unique_together = ('exam', 'position')  # Чтобы не было дубликатов номеров

    def __str__(self):
        return f"{self.exam.name} - {self.position}: {self.name}"

class Question(models.Model):
    LEVEL_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    admin = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='questions')
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE, related_name='questions')
    section = models.ForeignKey('subjects.SubjectSection', on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')
    question_text = models.TextField()
    image_path = models.CharField(max_length=255, null=True, blank=True)
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField(null=True, blank=True)
    option_4 = models.TextField(null=True, blank=True)
    option_5 = models.TextField(null=True, blank=True)
    correct_option = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    language_code = models.CharField(max_length=10)
    type = models.ForeignKey(QuestionType, on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return f"{self.question_text[:50]}..."