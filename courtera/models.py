from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Course(models.Model):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)  # comma-separated list
    ratings = models.FloatField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)  # JSON or plain text
    image_url = models.URLField(blank=True, null=True)
    course_link = models.URLField(blank=True, null=True)  # New field for course URL

    def __str__(self):
        return self.title
  
class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="user_courses")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # prevent duplicates

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"    