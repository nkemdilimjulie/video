from rest_framework import serializers
from video_qrcode_maker.models import VideoWithQRCode

class VideoWithQRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoWithQRCode
        fields = '__all__'