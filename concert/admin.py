from django.contrib import admin

# Register your models here.
from .models import Concert
from .models import ConcertAttending
admin.site.register(Concert)
admin.site.register(ConcertAttending)
