from django.db import models

# Create your models here.

class FireRecords(models.Model):
	name = models.CharField(max_length=30, default="manoj sharma")
	email = models.EmailField(default='manoj2sharma1996@gmail.com')
	Alarm_status = models.BooleanField(default=False)
	Created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return "Alarm status {} at {}".format(self.Alarm_status, self.Created_at)