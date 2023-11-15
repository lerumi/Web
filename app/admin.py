from django.contrib import admin
from .models import Tag, Question, answer, user
# Register your models here.
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(answer)
admin.site.register(user)