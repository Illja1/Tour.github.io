from django.contrib import admin
from .models import Category,Tour,RaitingStart,Raiting,Reviews
# Register your models here.
admin.site.register(Category)
admin.site.register(Tour)

admin.site.register(RaitingStart)
admin.site.register(Raiting)
admin.site.register(Reviews)
