from django.db import models

# Create your models here.

class main (models.model):
    id = models.AutoField(prymary_key=true)
    status = models.BooleanField('status', default=true)
    create_date =models.Datafield('creation date',auto_now=falce,auto_now_add=True)
    modify_date =models.Datafield('creation date',auto_now=falce,auto_now_add=True)