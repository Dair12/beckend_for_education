from django.db import models
from users.models import User
from user_tests.models import UserTest
from questions.models import Question

class UserAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(UserTest, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chosen_option_number = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_correct = models.BooleanField()
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer by {self.user.email} for question {self.question.id}"

    class Meta:
        db_table = 'user_answers'