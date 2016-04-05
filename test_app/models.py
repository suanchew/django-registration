# coding: utf-8

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUser(AbstractBaseUser):
    new_field = models.CharField(max_length=25)
    objects = BaseUserManager()

    USERNAME_FIELD = 'new_field'


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return (self.first_name + ", " + self.last_name)


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=30)
    tags = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text