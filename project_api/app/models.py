from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(null=False, blank=False, max_length=128)
    username = models.CharField(null=False, blank=False, max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(null=False, blank=False, max_length=128)
    website = models.CharField(null=False, blank=False, max_length=128)

    def __str__(self):
        return f'Username: {self.full_name} with id: {self.id}'


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(null=False, blank=False, max_length=128)
    suite = models.CharField(null=False, blank=False, max_length=128)
    city = models.CharField(null=False, blank=False, max_length=128)
    zipcode = models.CharField(null=False, blank=False, max_length=128)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.user.full_name} address, street: {self.street}'


class Task(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=128)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Task number {self.id} with title: {self.title}'
