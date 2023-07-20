from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, help_text=_("Title of the image"), verbose_name=_("Title"))
    description = models.CharField(max_length=250, blank=True, null=True, help_text=_("Captions of the image"), verbose_name=_("Captions of the image"))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date"))
    image = models.ImageField(upload_to="images/", blank=True, null=True, help_text=_("update the image"))

    def __str__(self):
        return self.title
    

    