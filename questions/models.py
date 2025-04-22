from django.db import models

class Question(models.Model):
    LEVEL_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey('users.User', on_delete=models.CASCADE)
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
    section = models.ForeignKey('subjects.SubjectSection', on_delete=models.SET_NULL, null=True, blank=True)
    question_text = models.TextField()
    image_path = models.CharField(max_length=255, null=True, blank=True)
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField(null=True, blank=True)
    option_4 = models.TextField(null=True, blank=True)
    option_5 = models.TextField(null=True, blank=True)
    correct_option = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    language_code = models.CharField(max_length=10)
    type = models.ForeignKey('QuestionType', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text[:50]

    class Meta:
        db_table = 'questions'

class QuestionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'question_types'