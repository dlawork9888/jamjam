# flip_detection/models.py

# Relation Schema

# flip_detection_id => AUTO INCREMENT, PK
# flip_score => float
# flip_time => date
# user_id => FK(from user table)

from django.db import models
from user.models import User # for FK

class FlipDetection(models.Model):
    flip_detection_id = models.AutoField(primary_key=True)  # AUTO INCREMENT, PK
    flip_score = models.FloatField()
    flip_time = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # FK(from user table), user table의 PK를 참조

    def __str__(self):
        return f"FlipDetection ID: {self.flip_detection_id}, Score: {self.flip_score}"