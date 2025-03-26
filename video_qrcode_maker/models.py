from django.db import models

class VideoWithQRCode(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    qr_code_data = models.TextField()
    processed_video = models.FileField(upload_to='processed_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)