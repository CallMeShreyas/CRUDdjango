from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=20)

    def __str__(self):
        return self.ename
    