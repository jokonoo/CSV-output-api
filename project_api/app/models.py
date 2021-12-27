from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(null=False, blank=False, max_length=128)

    def __str__(self):
        return f'User: {self.full_name} with id: {self.id}'


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(null=False, blank=False, max_length=128)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.user.full_name} address, city: {self.city}'


class Task(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=128)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Task number {self.id} with title: {self.title}'
