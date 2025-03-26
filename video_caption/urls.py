from django.urls import path
from .views import AddCaptionAPIView



urlpatterns = [
    path('add_caption/', AddCaptionAPIView.as_view(), name='add-caption'),
]
