from django.contrib import admin
from .models import Course

admin.site.register(Course, list_display=[
                    'course_name', 'contact_person', 'tel', 'school_id'])
