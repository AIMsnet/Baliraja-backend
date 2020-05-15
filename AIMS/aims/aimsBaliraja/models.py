from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

# Create your models here.


class User(AbstractUser):
    # username = None
    # mob_no   = models.CharField(max_length = 12, unique=True, null=False)
    address  = models.TextField()
    post     = models.CharField(max_length = 30)
    district = models.CharField(max_length = 30)
    taluka   = models.CharField(max_length = 30)

    # USERNAME_FIELD = 'mob_no'
        # REQUIRED_FIELDS = []
    class Meta:
        db_table = 'auth_user'


class Categories(models.Model):
    catagoryName    = models.CharField(max_length=100, unique=True)
    # catagoryImage   = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['svg'])])
    catagoryImage   = models.FileField(null=True, blank=True)
    # class Meta:
    #     db_table = 'aimsBaliraja_categories'