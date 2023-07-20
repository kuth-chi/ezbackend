from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    date_of_birth = models.DateField(blank=True, verbose_name=_('date of birth'), null=True)

    def __str__(self):
        return self.user
    

class PhoneNumber(models.Model):
    PHONELINE_CHOICES = (
        ('mobile', _('Mobile')),
        ('home', _('Home')),
        ('work', _('Work')),
        ('emergency', _('Emergency')),
    )
    phone_line = models.CharField(max_length=25, choices=PHONELINE_CHOICES, default="Mobile", verbose_name=_('Name'))
    phone_number = models.IntegerField(max_length=15, default="Mobile", verbose_name=_('Phone Number'))
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_('Updated Date'))

    def __str__(self):
        return self.phone_line