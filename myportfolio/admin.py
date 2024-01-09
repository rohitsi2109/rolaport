from django.contrib import admin
from myportfolio.models import Contact
# Register your models here.
admin.site.register(Contact)
from django.contrib import admin

admin.site.site_header = 'Rohit Singh Portfolio Admin Pannel'
admin.site.site_title = 'Rohit Singh Portfolio'
admin.site.index_title = 'Welcome to the portfolio Admin Panel'
