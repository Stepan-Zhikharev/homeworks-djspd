from django.contrib import admin

# зарегистрируйте необходимые модели
from main.models import Car, Client, Sale

admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Sale)

