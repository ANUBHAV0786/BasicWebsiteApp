from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class Questionnaire(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    form_link = models.URLField(blank=True, null=True)  # To store link if forms are hosted separately
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
