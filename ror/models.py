from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Person(models.Model):
    MRN = models.TextField(default='')
    name = models.TextField(default='')
    DOB = models.TextField(default='')
    status = models.TextField(default='')
    assigned = models.TextField(default='')


class Variant(models.Model):
    chromosome = models.TextField(default='')
    position = models.TextField(default='')
    rs_id = models.TextField(default='')
    ref = models.TextField(default='')
    alt = models.TextField(default='')
    gene = models.TextField(default='')
    func_type = models.TextField(default='')



    # python manage.py makemigrations
    # python manage.py migrate
