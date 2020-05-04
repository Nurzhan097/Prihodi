from django.conf import settings
from django.db import models


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', blank=True)
	description = models.TextField(blank=True, null=True, default=None)

	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return f'{self.user}'

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'

