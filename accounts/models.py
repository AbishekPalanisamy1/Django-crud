from django.db import models

# Create your models here.
class Accounts(models.Model):
    a_id=models.IntegerField()
    a_name=models.CharField(max_length=50)
    a_email=models.EmailField()
    a_contact=models.CharField(max_length=10)
    a_address=models.CharField(max_length=50,default='Unknown')

    def __str__(self):
        return '%s' %(self.a_id)
    
    class Meta:
        db_table='accounts'