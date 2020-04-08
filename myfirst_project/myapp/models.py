from django.db import models

# Create your models here.

class FireRecords(models.Model):
	name = models.CharField(max_length=30, default="manoj sharma")
	email = models.EmailField(default='manoj2sharma1996@gmail.com')
	sms_status = models.BooleanField(default=False)
	phone_number =  models.CharField(max_length=20, default="14372185806")
	sms_text = models.CharField(max_length=255, default="no text")
	Alarm_status = models.BooleanField(default=False)
	country = models.CharField(max_length=55, default="Canada")
	region = models.CharField(max_length=255, default="Ontario")
	city = models.CharField(max_length=55, default="Toronto")
	lat = models.CharField(max_length=55, default="43.6934")
	lon = models.CharField(max_length=55, default="-79.4857")

	Created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Alarm status {} at {}".format(self.Alarm_status, self.Created_at)