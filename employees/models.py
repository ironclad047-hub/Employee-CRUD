from django.db import models

class Employee(models.Model):
    full_name = models.CharField("ФИО", max_length=200)
    position = models.CharField("Должность", max_length=100)
    email = models.EmailField("Email", unique=True)
    photo = models.ImageField("Фото", upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.full_name