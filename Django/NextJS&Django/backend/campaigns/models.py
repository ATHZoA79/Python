from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    logo = CloudinaryField('Image',overwrite=True, format="jpg")
    
    class Meta:
        ordering=('-created_at')
      
    def __str__(self):
        return self.title
      
    def save(self, **args, **kwargs):
      to_assign = slugify(self.title)
      
