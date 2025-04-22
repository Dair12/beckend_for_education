from django.db import models
from users.models import User
from exams.models import Exam
from questions.models import Question

class UserTest(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    language_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Test {self.id} for {self.user.email}"

    class Meta:
        db_table = 'user_tests'

class TestQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(UserTest, on_delete=models.CASCADE, related_name='questions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Question {self.question.id} in Test {self.test.id}"

    class Meta:
        db_table = 'test_questions'