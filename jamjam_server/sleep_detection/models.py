# sleep_detection/models.py

# Relation Schema 

# sleep_detection_id => AUTO INCREMENT, PK
# blink_score => float
# move_socre => float
# sound_score => float
# sleep_result => float
# sleep_time => date
# user_id => FK (from user table)

from django.db import models

