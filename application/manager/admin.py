from django.contrib import admin
from manager.models import Content,Slide,Logos,location

class locationStyle(admin.ModelAdmin):
	list_display = ('title','lat','log','order')
	list_editable = ('lat','log','order')

class contentStyle(admin.ModelAdmin):
	filter_horizontal = ('slides','map_locations',"sponsors",)

class slidesStyle(admin.ModelAdmin):
	list_display = ('title','quote_text','order','show_logo')
	list_editable = ('order','show_logo')

admin.site.register(Content,contentStyle)
admin.site.register(Slide,slidesStyle)
admin.site.register(Logos)
admin.site.register(location,locationStyle)
