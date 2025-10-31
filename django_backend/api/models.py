from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base model with created/updated timestamps.
    """
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Note(TimeStampedModel):
    """
    A simple note with title and content.
    """
    title = models.CharField(max_length=255, db_index=True)
    content = models.Textarea = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-updated_at", "-created_at"]

    def __str__(self) -> str:
        return f"{self.title}"
