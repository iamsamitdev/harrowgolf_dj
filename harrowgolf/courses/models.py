from django.db import models
from django.utils import timezone


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    remark = models.CharField(max_length=255, blank=True)
    school_id = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.IntegerField()
