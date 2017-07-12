from django.db import models

# Create your models here.
class publication(models.Model):
    dept = models.CharField(max_length=100)
    title = models.CharField(max_length=200,unique=True )
    author = models.CharField(max_length=100)
    Journal_name =models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=[('conference', 'conference'), ('journal', 'journal')])
    nationality = models.CharField(max_length=100, choices=[('national','national'),('international','international')])
    page_no = models.CharField(max_length=50,blank=True)
    volume = models.IntegerField(blank=True)
    year = models.DateField()

    def __str__(self):
        return self.title + ' - ' + self.author


