import uuid
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Product category
class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    parent_category = models.ForeignKey('self', blank=True, null=True, verbose_name=_("Parent Category"), on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=100, blank=True, unique=True, verbose_name="slug")

    def generate_slug(self):
        if not self.slug:
            unique_id = str(uuid.uuid4())[:12]
            product_slug = slugify(self.name) + "-" + unique_id

            while ProductCategory.objects.filter(slug=product_slug).exists():
                unique_id = str(uuid.uuid4())[:12]
                product_slug = slugify(self.name) + "-" + unique_id
            
            self.slug = product_slug

    def save(self, *args, **kwargs):
        self.generate_slug()
        super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("name",)


    
# Product tags
class ProductTag(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    slug = models.SlugField(max_length=100, blank=True, unique=True, verbose_name=_("Slug"))

    def generate_tag_slug(self):
        if not self.slug:
            unique_id = str(uuid.uuid4())[:12]
            tag_slug = slugify(self.name) + '-' + unique_id

            while ProductTag.objects.filter(slug=tag_slug).exists():
                unique_id = str(uuid.uuid4())[:12]
                tag_slug = slugify(self.name) + '-' + unique_id
        
            self.slug = tag_slug

    def save(self, *args, **kwargs):
        self.generate_tag_slug()
        super(ProductTag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
    

    
# Product models
class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, help_text=_('Give a title for product'), verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'), help_text=_('Describe about product'))
    logo = models.ImageField(upload_to="products/logoes/", blank=True, verbose_name=_('Logo'))
    header = models.ImageField(upload_to="products/header/", blank=True, verbose_name=_('Header'))
    thumb = models.ImageField(upload_to="products/thumbnails/", blank=True, verbose_name=_('Thumbnail'))
    url = models.URLField(verbose_name=_('URL'), blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, blank=True, verbose_name=_('Slug'))
    tag = models.ManyToManyField(ProductTag, blank=True, related_name="products", verbose_name=_("Product Tag"))
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, related_name="product_category", blank=True, null=True)

    # Generate a unique slug
    def generate_product_slug(self):
        if not self.slug:
            unique_id = str(uuid.uuid4())[:12]
            product_slug = slugify(self.title) + "-" + unique_id

            while Product.objects.filter(slug=product_slug).exists():
                unique_id = str(uuid.uuid4())[:12]
                product_slug = slugify(self.title) + "-" + unique_id
            self.slug = product_slug

    # Save slu to database
    def save(self, *args, **kwargs):
        self.generate_product_slug()
        super(Product, self).save(*args, **kwargs)

    # for admin site
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("-created_date",)


# Product Image Gallery
class ProductImageGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name="product_images_gallery")
    image = models.ImageField(upload_to="products/gallery/", blank=True, null=True, help_text=_("Upload image for product"))

    class Meta:
        verbose_name = "ProductImageGallery"
        verbose_name_plural = "ProductImageGallies"



# Pricing for product
class ProductPrice(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="product_price", verbose_name=_("product"))
    base_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, verbose_name=_("Base Price"))
    created_date = models.DateTimeField(auto_now_add=True)
    expired_date = models.DateTimeField(blank=True, verbose_name=_("Expired Date"))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.base_price)
    
# Product Discount
class ProductDiscount(models.Model):
    discount_value = models.IntegerField(default=0, blank=True, verbose_name=_("Discount Value"))
    discount_unit = models.IntegerField(default=0, blank=True, verbose_name=_("Discount Unit"))
    valid_until = models.DateTimeField(blank=True, verbose_name=_("Valid until"))
    coupon_code = models.CharField(max_length=15, blank=True, verbose_name=_("Coupon Code"))
    minimun_order_value = models.IntegerField(default=0, blank=True, verbose_name=_("Minimum Order Value"))
    maximum_discount_amount = models.IntegerField(default=0, blank=True, verbose_name=_("Maximum Discount Amount"))
    is_redeem_allowed = models.BooleanField(default=False)
    product = models.ForeignKey(Product, related_name="product_discount", on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Product Discount"))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.discount_value)
    