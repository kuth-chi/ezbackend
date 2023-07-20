from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Title"))
    description = models.TextField(max_length=2500, blank=True, null=True, verbose_name=_("Description"))
    url = models.URLField(blank=True, null=True, verbose_name=_("URL"))
    logo = models.ImageField(upload_to="services/logo", blank=True, null=True, verbose_name=_("Logo"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    edited_at = models.DateTimeField(auto_now=True, verbose_name="Edited At")

    def __str__(self):
        return self.title