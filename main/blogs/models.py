import uuid
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Categorizing models
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Category"))
    slug = models.SlugField(unique=True, blank=True, verbose_name=_("Slug"))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')

    def slug_category(self):
        if not self.slug:
            unique_id = str(uuid.uuid4())[:6]
            validate_slug = slugify(self.name + "-" + unique_id)

            while Category.objects.filter(slug=validate_slug).exists():
                unique_id = str(uuid.uuid4())[:12]
                validate_slug = slugify(self.name + "-" + unique_id)

            self.slug = validate_slug

    def save(self, *args, **kwargs):
        self.slug_category()
        super(Category, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ('name',)


# Tagging models
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=75, unique=True, blank=True, verbose_name=_("Slug"))
    
    def create_tag_slug(self):
        if not self.slug:
            tag_slug = slugify(self.name)[:50]  # Limit the slug to 50 characters

            while Tag.objects.filter(slug=tag_slug).exists():
                unique_id = str(uuid.uuid4())[:6]  # Generate a random 6-character ID
                tag_slug = slugify(self.name)[:50] + "-" + unique_id

            self.slug = tag_slug

    def save(self, *args, **kwargs):
        self.create_tag_slug()
        super(Tag, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


# Create blog post model
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=200, verbose_name=_("Subtitle"))
    header_image = models.ImageField(upload_to="media/blogs/header", blank=True, verbose_name=_('Header Image'), help_text=_("Size = 1500px x 500px"))
    thumbnail = models.ImageField(upload_to="media/blogs/thumbs", blank=True, verbose_name=_('Thumbnail'), help_text=_("Size = 405px x 305px"))
    content = models.TextField(verbose_name=_("Content"))
    category = models.ForeignKey(Category, related_name="blog_posts", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Category"))
    tags = models.ManyToManyField(Tag, related_name="blog_posts", blank=True, verbose_name=_("Tags"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    authors = models.ManyToManyField(User, related_name="blog_posts", verbose_name=_("Authors"))
    editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="edited_blog_posts", verbose_name=_("Editor"))
    slug = models.SlugField(max_length=75, unique=True, verbose_name=_("Slug"))

    def create_blog_slug(self):
        if not self.slug:
            unique_id = str(uuid.uuid4())[:6]  # Corrected slicing notation here
            validate_slug = slugify(self.title + unique_id)

            while BlogPost.objects.filter(slug=validate_slug).exists():
                unique_id = str(uuid.uuid4())[:6]  # Corrected slicing notation here
                validate_slug = slugify(self.title + unique_id)

            self.slug = validate_slug

    def save(self, *args, **kwargs):
        self.create_blog_slug()
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)


