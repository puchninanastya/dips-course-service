from django.db import models

class Course(models.Model):
    name = models.CharField(
        max_length=60,
        blank=False,
        verbose_name="Name")
    description = models.TextField(
        blank=True,
        default='',
        verbose_name="Description")
    start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name= "Start date")
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name= "End date")
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return "{}".format(self.name)
