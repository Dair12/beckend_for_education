from django.db import models

class Exam(models.Model):
    exam_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    has_fixed_structure = models.BooleanField(default=False)
    default_question_count = models.IntegerField()
    time_to_complete = models.IntegerField()  # В минутах
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'exams'

    def __str__(self):
        return f"{self.name} ({self.exam_code})"