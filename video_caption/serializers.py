from rest_framework import serializers
from video_caption.models import VideoWithCaption

class VideoWithCaptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoWithCaption
        fields = '__all__'