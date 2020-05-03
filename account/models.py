from django.db import models


class Profile(models.Model):
	name = models.CharField(max_length=120)
	avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', blank=True)
	description = models.TextField()

	# is_active =

