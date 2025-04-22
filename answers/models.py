from django.db import models
from django.conf import settings


class UserAnswer(models.Model):
    test = models.ForeignKey('tests.UserTest', on_delete=models.CASCADE)
    variant_question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chosen_option_number = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_correct = models.BooleanField(null=True)
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_answers'

    def __str__(self):
        return f"Answer by {self.user.email} for question {self.variant_question.id}"