from django.db import models

# Create your models here.

class Departments(models.Model):
    DEPT_NAME = (
        (0, '-----'),
        (1, 'Operations'),
        (2, 'Human Resources'),
        (3, 'Finance'),
        (4, 'Marketing'),
        (5, 'Sales'),
        (6, 'Information Technology')
    )

class Genders(models.Model):

    GENDER_TYPE = (
        (0, '-----'),
        (1, 'Female'),
        (2, 'Male'),
        (3, 'Not Specified')
    )