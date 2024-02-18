from djongo import models
from django.contrib.auth import get_user_model

User=get_user_model()

class FamilyMember(models.Model):
    name = models.CharField(max_length=200)
    relation = models.CharField(max_length=200)
    age = models.IntegerField()
    occupation = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    resident = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
         db_table='family_members'


class Vehicles(models.Model):
    vehicle = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    registration_no = models.IntegerField()
    use = models.CharField(max_length=200)
    sticker = models.BooleanField(default=True)
    resident = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
         db_table='vehicles'


class Pets(models.Model):
    name = models.CharField(max_length=200)
    registered = models.BooleanField(default=True)
    registration_no = models.IntegerField()
    resident = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
         db_table='pets'


class Harper(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    police_verification = models.BooleanField(default=True)
    contact = models.CharField(max_length=12)
    resident = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)


    def __str__(self):
        return self.title
    
    class Meta:
         db_table='harper'
