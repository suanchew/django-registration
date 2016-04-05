from django.contrib import admin

from .models import User, Post, Question, Choice

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Choice)
