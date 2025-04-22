from django.db import models

class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    exam_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    has_fixed_structure = models.BooleanField(default=False)
    default_question_count = models.IntegerField()
    time_to_complete = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'exams'