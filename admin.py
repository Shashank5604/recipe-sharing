from django.contrib import admin
from food.models import cservice
from food.models import popular,atendance
from food.models import bookings,student,Like

admin.site.register(Like)
admin.site.register(student)
admin.site.register(atendance)

class contact3(admin.ModelAdmin):
    list_display=('name','email','subject','message')

admin.site.register(cservice,contact3)

class tables(admin.ModelAdmin):
    list_display=('bname','bemail','bdtime','bpeople','brequest')

admin.site.register(bookings,tables)

class fpopular(admin.ModelAdmin):
    list_display=('foodname','foodimage','foodprice','foodmessage')

admin.site.register(popular,fpopular)