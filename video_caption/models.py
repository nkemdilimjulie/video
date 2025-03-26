from django.db import models


class VideoWithCaption(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    caption_text = models.TextField()
    processed_video = models.FileField(upload_to='processed_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
