from random import choice

from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
from parking_transactions.models import Employees, Vehicles, Transactions, DepartmentPositions, Genders

fake = Faker()

class Command(BaseCommand):
    help = 'Generate employee, their vehicles, and its transactions.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--employees',
            type=int,
            default=5,
            help='Number of employees to generate (default = 5)',
        )

        parser.add_argument(
            '--vehicles',
            type=int,
            default=2,
            help='Number of vehicles each employee owns (default = 2',
        )

        parser.add_argument(
            '--transactions',
            type=int,
            default=3,
            help='Number of transaction per vehicle (default = 2)',
        )
    def handle(self, *args, **kwargs):

        numof_employees = kwargs['employees']
        numof_vehicles = kwargs['vehicles']
        numof_transac = kwargs['transactions']

        # self.style.SUCCESS for green text
        # self.style.ERROR for red text
        # self.style.WARNING for yellow text
        # self.style.NOTICE for neutral text

        self.stdout.write(self.style.SUCCESS(f'Creating {numof_employees} employees, each owning {numof_vehicles} vehicles, with each having {numof_transac} transactions.'))

        for _ in range(numof_employees):

            employee = Employees.objects.create(
                employee_name = fake.name(),
                # employee_gender = fake.random_element(choice[0] for choice in Genders.GENDER_TYPE),
                employee_gender=fake.random_element([0,1]),
                employee_post = DepartmentPositions.objects.order_by('?').first()
            )

            for _ in range(numof_vehicles):

                vehicle = Vehicles.objects.create(
                    vehicle_emp = employee,
                    vehicle_plate = fake.bothify(text='???-####', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                    vehicle_type = fake.random_element([0,1,2,3,4])
                )

                for _ in range(numof_transac):
                    transac_state = fake.random_element([0,1,2,3])

                    if transac_state == 1:
                        transac_date = fake.date_between(start_date='today', end_date='+1w')
                    else:
                        transac_date = fake.date_between(start_date='-1w', end_date='today')

                    transac = Transactions.objects.create(
                        txn_plate = vehicle,
                        txn_state = transac_state,
                        txn_date = transac_date,
                    )