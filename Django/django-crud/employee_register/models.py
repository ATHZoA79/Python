from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField( max_length=50)

    def __str__(self):
        # the Foreign key will show title as default output
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    # Relation to other model
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

