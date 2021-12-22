from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(null=False, blank=False, max_length=128)
    username = models.CharField(null=False, blank=False, max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(null=False, blank=False, max_length=128)
    website = models.CharField(null=False, blank=False, max_length=128)


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(null=False, blank=False, max_length=128)
    suite = models.CharField(null=False, blank=False, max_length=128)
    city = models.CharField(null=False, blank=False, max_length=128)
    zipcode = models.CharField(null=False, blank=False, max_length=128)


class Geo(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)
    lat = models.FloatField()
    lng = models.FloatField()


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, max_length=128)
    catch_phrase = models.TextField(null=False, blank=False, max_length=512)
    bs = models.TextField(null=False, blank=False, max_length=128)


class Task(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=128)
    completed = models.BooleanField(default=False)











