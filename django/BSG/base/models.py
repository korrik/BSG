# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm

class User(AbstractUser):
    term = models.IntegerField(default = 1)

class BusinessProject(models.Model):
    user = models.ForeignKey(User)
    key_partners = models.CharField(max_length=200)
    key_values = models.TextField()

class DataforInvestor(models.Model):
    tam_choices =  (
        ('L','Бюджетный'),
        ('M','Средний'),
        ('P','Премиальный'),
    )

    sam_choices = (
        ('R','Россия'),
        ('U','США'),
        ('C','Китай'),
        )

    user = models.ForeignKey(User)
    idea_and_product = models.CharField(max_length = 500)
    market_capacity = models.CharField(max_length = 500)
    competitors = models.CharField(max_length = 500)
    costs = models.CharField(max_length = 500)
    investements = models.CharField(max_length = 500)
    SAM_number = models.IntegerField()
    SOM_number = models.IntegerField()
    TAM_field = models.CharField(max_length = 25, choices = tam_choices, default = 'L')
    SAM_field = models.CharField(max_length = 25, choices = sam_choices, default = 'R')
