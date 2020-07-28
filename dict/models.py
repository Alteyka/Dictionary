import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Word(BaseModel):
    name = models.CharField(max_length=200)
    translate = models.CharField(max_length=200)
    transcription = models.CharField(max_length=200)
    phrase = models.CharField(max_length=200)
    sentence = models.CharField(max_length=200)

    def __str__(self):
        return self.name

