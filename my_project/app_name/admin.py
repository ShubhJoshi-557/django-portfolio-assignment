from django.contrib import admin
#/------Django Internal Packages-----

#------Django Importing Models-----
from app_name.models import ContactForm
#/------Django Importing Models-----

#Register your models here.

#-----Django Admin View for ----

#Django Admin View for Contact Form Model
class ContactFormkAdmin(admin.ModelAdmin):
    search_fields = ["pk","full_name"]
    list_filter = ["full_name"]
    list_display = [
        "pk",
        'created_at',
        "full_name",
        "email_id",
        "contact_number",
        "message",
    ]
    list_editable = ["full_name"]

#Register ContactForm in Admin view 
admin.site.register(ContactForm,ContactFormkAdmin)
