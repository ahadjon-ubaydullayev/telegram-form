from django.db import models

class UserRequest(models.Model):
	user_id = models.CharField(max_length=255)
	step = models.IntegerField(default=0)

	def __str__(self):
		return self.user_id


