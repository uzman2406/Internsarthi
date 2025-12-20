from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField(blank=True)
    preferred_role = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username



class Internship(models.Model):
    internship_id = models.BigIntegerField(unique=True)
    role = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    stipend = models.CharField(max_length=100)
    intern_type = models.CharField(max_length=255)
    skills = models.TextField()
    perks = models.TextField()
    website_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.role} - {self.company_name}"


class SavedInternship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'internship')

    def __str__(self):
        return f"{self.user.username} saved {self.internship.role}"
    
class AppliedInternship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'internship')

    def __str__(self):
        return f"{self.user.username} applied to {self.internship.role}"
