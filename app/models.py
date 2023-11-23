from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=1111111)
    email=models.CharField(max_length=1111111)
    desc=models.TextField(max_length=100000)
    

    class Meta:
        verbose_name_plural = "Person"
    def str(self):
        return self.name




