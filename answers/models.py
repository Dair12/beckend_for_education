from django.db import models
from users.models import User

class UserAnswer(models.Model):
    test = models.ForeignKey('user_tests.UserTest', on_delete=models.CASCADE)
    variant_question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # !!! здесь
    chosen_option_number = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_correct = models.BooleanField(null=True)
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_answers'
