from django.contrib import admin
from .models import Seminars,Profile,ContactUs,SharkTank,OldSharkTank,eventsUpcoming

# Register your models here.

admin.site.register(OldSharkTank)
admin.site.register(SharkTank)
admin.site.register(Seminars)
admin.site.register(Profile)
admin.site.register(ContactUs)
admin.site.register(eventsUpcoming)
