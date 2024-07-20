from django.contrib import admin
from home_app.models import registration_table,login_table

# Register your models here.
admin.site.register(registration_table)
admin.site.register(login_table)

