import random, string, uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify 

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Title"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    url = models.URLField(blank=True, null=True, verbose_name=_("URL"))
    logo = models.ImageField(upload_to="services/logo", blank=True, null=True, verbose_name=_("Logo"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    edited_at = models.DateTimeField(auto_now=True, verbose_name="Edited At")
    slug = models.SlugField(unique=True, blank=True, null=True, help_text=_("Slug for the service"))

    def generate_slug(self):
            if not self.slug:
                random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
                unique_id = str(uuid.uuid4())[:10]
                candidate_slug = slugify(random_chars + unique_id + self.title)

                # Check if the generated slug is unique, if not, regenerate until it's unique
                while Service.objects.filter(slug=candidate_slug).exists():
                    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
                    unique_id = str(uuid.uuid4())[:10]
                    candidate_slug = slugify(random_chars + unique_id + self.title)

                self.slug = candidate_slug

    def save(self, *args, **kwargs):
        self.generate_slug()
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

# Image for service    
class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="products/images/", help_text=_("Upload product image"), verbose_name=_("Image"))
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service.title} - Image {self.id}"
    
class ServicePrice(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='service_price', blank=True, null=True)
    service_name = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("Service Name"))
    service_badge = models.ImageField(upload_to="services/badge/", help_text=_("Upload badge icon for service"), verbose_name=_("Service Badge"))
    CURRENCY_CHOICES = (
        ('kmr', _('KHR')),
        ('usd', _('USD')), 
    )
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, verbose_name=_("Price"))
    currency = models.CharField(max_length=3, default="USD", choices=CURRENCY_CHOICES, verbose_name=_("Currency"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    timestamp = models.DateTimeField(auto_now_add=True)