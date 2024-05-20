from django.db import models

# Create your models here.

class StuModel(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    class Meta():
        verbose_name_plural = 'Student_List'
    def __str__(self):
        return str(self.Name)