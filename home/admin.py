from django.contrib import admin
from home.models import Admin, customer, booking, Event
# Register your models here.
admin.site.register(Admin)
admin.site.register(customer)
admin.site.register(Event)
admin.site.register(booking)
