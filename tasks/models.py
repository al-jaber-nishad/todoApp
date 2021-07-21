from django.db import models

# Create your models here.

class task_info(models.Model):
  title = models.CharField(verbose_name="Title", max_length=50,)
  details = models.CharField(verbose_name="Details", max_length=256, blank=True)
  complete = models.BooleanField()

  def __str__(self):
      return self.title
  