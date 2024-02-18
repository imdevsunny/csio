from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
import uuid
# Create your models here.

class User(AbstractUser):

    username=None
    phone=models.CharField(_("Phone Number"), max_length=13, unique=True)
    # email=models.EmailField(_("Email Address"), max_length=254, unique=True)
    house_number=models.IntegerField(_("House No."),null=True, blank=True)
    allottee_name=models.CharField(_("Allottee Name"), max_length=255, null=True, blank=True)
    id_number=models.UUIDField(_("ID Number"), default=uuid.uuid4, primary_key=False, editable=False)

    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=[]
    objects=UserManager()
