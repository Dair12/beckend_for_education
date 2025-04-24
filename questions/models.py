from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from exam_sections.models import Section

class Question(models.Model):
    LEVEL_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    admin = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='questions')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions')
    position = models.PositiveIntegerField()  # Ensure this field is present
    question_text = models.TextField()
    description = models.TextField(null=True, blank=True)
    question_image = models.BinaryField(null=True, blank=True)
    description_image = models.BinaryField(null=True, blank=True)
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField(null=True, blank=True)
    option_4 = models.TextField(null=True, blank=True)
    option_5 = models.TextField(null=True, blank=True)
    correct_option = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    language_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'questions'
        unique_together = ('section', 'position')  # Ensure this is correct

    def __str__(self):
        return f"{self.question_text[:50]}..."