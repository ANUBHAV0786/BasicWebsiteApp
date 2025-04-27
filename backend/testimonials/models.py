from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='testimonial_photos/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
