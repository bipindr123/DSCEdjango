from django.db import models


# Create your models here.
class publication(models.Model):
    dept = models.CharField("Department(full name)",max_length=100)
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    Journal_name = models.CharField("Journal/Conference Name",max_length=100)
    type = models.CharField(max_length=100, choices=[('conference', 'conference'), ('journal', 'journal')])
    nationality = models.CharField(max_length=100,
                                   choices=[('national', 'national'), ('international', 'international')])
    page_no = models.CharField(max_length=50, blank=True,null=True)
    volume = models.IntegerField(blank=True,null=True)
    year = models.DateField()
    impact_factor = models.CharField(max_length=200, blank=True, null=True)
    citations = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.title + ' - ' + self.author
