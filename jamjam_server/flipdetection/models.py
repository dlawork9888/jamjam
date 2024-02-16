# flipdetection/models.py

from django.db import models
from django.contrib.auth.models import User

class FlipDetection(models.Model):
    flipdetection_id = models.AutoField(primary_key=True)
    flip_score = models.FloatField()
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    #def __str__(self):
    #    return f"FlipDetection ID: {self.flipdetection_id}, Flip Score: {self.flip_score}, User ID: {self.user_id}"
