from django.db import models

class Section(models.Model):
    exam = models.CharField(max_length=255)  # Название экзамена
    subject = models.CharField(max_length=100)  # Название предмета
    section = models.CharField(max_length=100)  # Название раздела
    exam_code = models.CharField(max_length=50)  # Код экзамена (ЕГЭ, ОРТ, SAT)
    has_fixed_structure = models.BooleanField(default=False)  # Имеет ли фиксированную структуру
    default_question_count = models.IntegerField()  # Количество вопросов по умолчанию
    time_to_complete = models.IntegerField()  # Время на выполнение в минутах

    class Meta:
        db_table = 'sections'  # Имя таблицы в базе данных

    def __str__(self):
        return f"{self.exam} - {self.subject} - {self.section}"