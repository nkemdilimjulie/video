from django.urls import path
from .views import EmbedQRCodeAPIView

urlpatterns = [
     path('embed_qr/', EmbedQRCodeAPIView.as_view(), name='embed-qr'),
]
