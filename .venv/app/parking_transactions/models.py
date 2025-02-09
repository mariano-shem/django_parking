import uuid
import datetime

from django.db import models
from django.utils import timezone
from libraries.models import Departments, Genders

# Create your models here.

class Employees(models.Model):

    employee_id = models.UUIDField(
        db_column='employee_id',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    employee_name = models.CharField(
        db_column='employee_name',
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Employee Name'
    )

    employee_gender = models.IntegerField(
        db_column='employee_gender',
        choices=Genders.GENDER_TYPE,
        default=0,
        verbose_name='Employee Gender'
    )

    employee_dept = models.IntegerField(
        db_column='employee_dept',
        choices=Departments.DEPT_NAME,
        default=0,
        verbose_name='Employee Department'
    )

    employee_post = models.CharField(
        db_column='employee_post',
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Employee Position'
    )


    def __str__(self):
        return str(self.employee_name)

    class Meta:
        db_table = 'tbl_employees'
        verbose_name_plural = 'Employees'
        verbose_name = 'Employee'


class Vehicles(models.Model):

    VEHICLE_TYPE=(
        (0, 'CAR'),
        (1, 'MOTORCYCLE'),
        (2, 'BICYCLE'),
        (3, 'SCOOTER'),
        (4, 'E-BIKE')
    )

    vehicle_id = models.AutoField(
        db_column='vehicle_id',
        primary_key=True,
        editable=False
    )

    vehicle_emp = models.ForeignKey(
        Employees,
        db_column='vehicle_emp_id',
        on_delete=models.CASCADE,
        related_name='vehicle_emp',
        verbose_name="Vehicle Owner"
    )

    vehicle_plate = models.CharField(
        db_column='vehicle_plate',
        max_length=8,
        blank=False,
        null=False
    )

    vehicle_type = models.IntegerField(
        db_column='vehicle_type',
        choices=VEHICLE_TYPE,
        default=0
    )

    def __str__(self):
        return str(self.vehicle_plate)

    class Meta:
        db_table = 'tbl_vehicles'
        verbose_name_plural = 'Vehicles'
        verbose_name = 'Vehicle'

class Transactions(models.Model):
    VEHICLE_STATE=(
        (0, 'Parked'),
        (1, 'Reserved'),
        (3, 'In Transit'),
        (4, 'Charging')
    )

    txn_id = models.AutoField(
        db_column='txn_id',
        primary_key=True,
        editable=False
    )

    txn_plate = models.ForeignKey(
        Vehicles,
        db_column='txn_plate_id',
        on_delete=models.CASCADE,
        related_name='txn_plate'
    )

    txn_state = models.IntegerField(
        db_column='txn_state',
        choices=VEHICLE_STATE,
        default=0
    )

    txn_date = models.DateField(
        db_column='txn_date',
        null=False
    )

    txn_created = models.DateTimeField(
        db_column='txn_created',
        auto_now_add=True
    )

    txn_updated = models.DateTimeField(
        db_column='txn_updated',
        auto_now=True
    )

    def __str__(self):
        return str(self.txn_id)

    class Meta:
        db_table = 'tbl_transactions'
        verbose_name_plural = 'Transactions'
        verbose_name = 'Transaction'
