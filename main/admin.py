from django.contrib import admin
from .models import *
from .forms import PropertyForm,RoomForm,ImageForm
from django.utils.translation import ugettext_lazy

admin.site.site_title = ugettext_lazy('Property233')
admin.site.site_header = ugettext_lazy('Property233')
admin.site.index_title = ugettext_lazy('Property233')

class ImageInline(admin.StackedInline):
    model = Image
    extra = 2

class RoomInline(admin.StackedInline):
    model = Room
    extra = 2

class PriceInline(admin.StackedInline):
    model = Price
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    form = PropertyForm
    inlines = [PriceInline,RoomInline,ImageInline]
    prepopulated_fields = {'slug': ('owner','type','location')}

    def save_model(self, request, obj, form, change):
        super(PropertyAdmin,self).save_model(request, obj, form, change)
        # obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.images.create(file=afile)