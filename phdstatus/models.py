from django.db import models


class PhdStatus(models.Model):
    name = models.CharField("Research Scholar Name", max_length=200)
    dept = models.CharField("Department", max_length=200)
    guide = models.CharField("Guide", max_length=200)
    uni = models.CharField("University where registered", max_length=200)
    synopsys = models.CharField(max_length=50,blank=True, choices=[('approved', 'approved'), ('not approved', 'not approved')])
    year = models.DateField("year of registration")
    status = models.CharField("status", max_length=50,
                              choices=[('Completed', 'Completed'), ('OnGoing', 'OnGoing')])
    other = models.TextField("Any other details", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Ph.D Status"

    def __str__(self):
        return self.name + ' - ' + self.dept


class WorkStatusTable(models.Model):
    phdstatus = models.ForeignKey(PhdStatus, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField("title", max_length=100, blank=True, null=True)
    status = models.CharField("status", max_length=50, choices=[('Yes', 'yes'), ('No', 'no')])

    class Meta:
        verbose_name_plural = "Course Work Status"

    def __str__(self):
        return self.title


class ComprehensiveTable(models.Model):
    phdstatus = models.OneToOneField(PhdStatus, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField("title", max_length=300, blank=True, null=True)
    status = models.CharField("status", max_length=50,
                              choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed')])

    class Meta:
        verbose_name_plural = "Comprehensive viva voce"
        verbose_name = "Comprehensive viva voce"

    def __str__(self):
        return self.title


class WorkshopsTable(models.Model):
    phdstatus = models.ForeignKey(PhdStatus, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField("title", max_length=300, blank=True, null=True)
    duration = models.IntegerField("Duration(Days)", blank=True, null=True)
    details = models.CharField("Details", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Workshops/seminar/conference attended"

    def __str__(self):
        return self.title


class TrainingTable(models.Model):
    phdstatus = models.ForeignKey(PhdStatus, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField("title", max_length=300, blank=True, null=True)
    duration = models.IntegerField("Duration(Days)", blank=True, null=True)
    details = models.CharField("Details", max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = "Any other training"

    def __str__(self):
        return self.title


class FundedProjectsTable(models.Model):
    phdstatus = models.ForeignKey(PhdStatus, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField("title", max_length=300, blank=True, null=True)
    funding_sought = models.IntegerField("Funding sought", blank=True, null=True)
    funding_agency = models.CharField("Funding Agency", max_length=50, blank=True, null=True)
    submitted_date = models.DateField("Submitted Date", blank=True, null=True)
    status = models.CharField("status", max_length=50,
                              choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed')])

    class Meta:
        verbose_name = "Proposals submitted relating to the Research Topic"

    def __str__(self):
        return self.title
