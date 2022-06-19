from django.db import models
#from ckeditor .fields import RichTextField
# Create your models here.

#ID is automatically created
class Publication(models.Model):
    title = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    series_name = models.CharField(max_length=255)
    pub_format = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    publication_date = models.DateField(null=True)
    ISBN_13 = models.CharField(max_length=30, blank=True)
    ISBN_10 = models.CharField(max_length=30, blank=True)
    ISBN_registered = models.BooleanField()
    ISBN_url = models.URLField(blank=True)
    #note = RichTextField(blank=True, null=True)
    note = models.TextField()

#    class Meta:
#        ordering = ('-id', )

    def __str__(self):
        return self.title

class Register(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email