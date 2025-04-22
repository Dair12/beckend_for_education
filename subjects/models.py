from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'subjects'

    def __str__(self):
        return self.name

class SubjectSection(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'subject_sections'

    def __str__(self):
        return f"{self.subject.name} - {self.name}"