from django.db import models
from users.models import User
from exam_sections.models import Section  # Новый импорт
from questions.models import Question

class UserTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tests')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='user_tests')  # Замена exam на section
    language_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'user_tests'

    def __str__(self):
        return f"Test {self.id} for {self.user.name} - {self.section.exam} - {self.section.subject}"

class TestQuestion(models.Model):
    test = models.ForeignKey(UserTest, on_delete=models.CASCADE, related_name='test_questions')
    variant_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_order = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'test_questions'

    def __str__(self):
        return f"Question {self.variant_question.id} in Test {self.test.id}"