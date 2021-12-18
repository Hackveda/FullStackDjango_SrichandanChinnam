from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=10, default='admin')
    last_name = models.CharField(max_length=10, default='admin' )
    address = models.CharField(max_length=50, default='Delhi')
    pincode = models.IntegerField(default=123434)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + " " +self.address + " " + str(self.pincode)
