from django.contrib import admin
from form.models import *



@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'born_date', 'current_state_education', 'education_place', 'marital_status', 'address_province', 'address_region_full', 'workplace', 'rank', 'tel_number', 'work_experience', 'it_level', 'languages']

