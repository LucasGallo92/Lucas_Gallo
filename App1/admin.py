from django.contrib import admin

# Register your models here.
from .models import BronzeSaint, SilverSaint, GoldSaint

admin.site.register(BronzeSaint)
admin.site.register(SilverSaint)
admin.site.register(GoldSaint)