from django.contrib import admin

from . models import profile # you are saying take from model.py from that script take profile aka inheritance...

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile

admin.site.register(profile,profileAdmin)
# Register your models here.
