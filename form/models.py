from django.db import models


class Applicant(models.Model):
	user_id = models.IntegerField(unique=True)
	step = models.IntegerField(default=0)
	full_name = models.CharField(max_length=256, blank=True, null=True)
	born_date = models.CharField(max_length=128, blank=True, null=True)
	current_state_education = models.CharField(max_length=64, blank=True, null=True)
	education_place = models.CharField(max_length=1024, blank=True, null=True)
	marital_status = models.CharField(max_length=64, blank=True, null=True)
	address_province = models.CharField(max_length=128, blank=True, null=True)
	address_region_full = models.CharField(max_length=128, blank=True, null=True)
	workplace = models.CharField(max_length=512, blank=True, null=True)
	rank = models.CharField(max_length=512, blank=True, null=True)
	tel_number = models.CharField(max_length=512, blank=True, null=True)
	active = models.BooleanField(default=False)
	work_experience = models.CharField(max_length=256, blank=True, null=True)
	it_level = models.CharField(max_length=256, blank=True, null=True)
	languages = models.CharField(max_length=256, blank=True, null=True)

	def __str__(self):
		return self.full_name




class Rank(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

