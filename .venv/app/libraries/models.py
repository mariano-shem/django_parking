from django.db import models

# Create your models here.

class DepartmentPositions(models.Model):

    dept_post_id = models.AutoField(db_column='dept_post_id', primary_key=True, editable=False)
    dept_post = models.CharField(db_column='dept_post', max_length=32, null=False, blank=False)
    dept_name = models.CharField(db_column='dept_name', max_length=32, null=False, blank=False)

    def __str__(self):
        return str(self.dept_post)

    class Meta:
        db_table = 'tbl_deptpositions'
        verbose_name_plural = 'DepartmentPositions'
        verbose_name = 'DepartmentPosition'

class Genders(models.Model):

    GENDER_TYPE = (
        (0, '-----'),
        (1, 'Female'),
        (2, 'Male'),
        (3, 'Not Specified')
    )