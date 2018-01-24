from django.db import models

class Token(models.Model):
    client_id = models.CharField(max_length=40)
    client_secret = models.CharField(max_length=128)
    token = models.CharField(max_length=30, null=True)
    expires = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def __str__(self):
        return "Toker for cliend id: {}".format(self.client_id)

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
