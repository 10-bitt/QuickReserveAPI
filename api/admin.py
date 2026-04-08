from django.contrib import admin
from .models import User, Facility, Reservation

admin.site.register(User)
admin.site.register(Facility)
admin.site.register(Reservation)