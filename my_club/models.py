from django.db import models


# Create your models here.

class member(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    position= models.CharField(null=True, blank=True, max_length=255)
    description=models.TextField(null=True, blank=True)
    address= models.TextField()
    join_date=models.DateField(auto_now_add=True)
    photo=models.ImageField(null=True, blank=True, upload_to= 'media/')
    fees=models.IntegerField(default=200)

    def __str__ (self):
        return str(self.name)+"|"+str(self.category)+"|"+str(self.position)


