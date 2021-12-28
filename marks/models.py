from django.db import models

class Student(models.Model):
    name = models.TextField(default='')
    email = models.TextField(default='')
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')

    # class Meta:
    #     db_table = 'Student'

class Marks(models.Model):
    stu_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    maths = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    biology = models.IntegerField(default=0)
    english = models.IntegerField(default=0)

    # class Meta:
    #     db_table = 'marks'