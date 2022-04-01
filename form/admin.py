from django.contrib import admin
from form.models import *



@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    pass