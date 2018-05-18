from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField() # May 17, 2018, 4:01 p.m.
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title # Gives better name to posts listed in admin page.

    # Allows usage in html templates by referencing function name.
    def pub_date_pretty(self):
        # %e should be %d if on Windows machine 
        return self.pub_date.strftime('%b %e %Y') # May 17 2018

    def summary(self):
        return self.body[:100]