from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name} {self.phone_number}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=50)
    year = models.SmallIntegerField()
    color = models.CharField(max_length=15)
    mileage = models.IntegerField()
    volume = models.DecimalField(max_digits=2, decimal_places=1)
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES)
    drive_unit = models.CharField(max_length=20, choices=DRIVE_UNIT_CHOICES)
    gearbox = models.CharField(max_length=20, choices=GEARBOX_CHOICES)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
            return f"{self.model} {self.year}"


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ManyToManyField('Client')
    car = models.ManyToManyField('Car')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Sale - {self.id} at {self.created_at} {self.client}'

