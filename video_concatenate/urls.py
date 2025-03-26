from django.urls import path
from .views import ConcatenateVideosAPIView

urlpatterns = [
    path('concatenate/', ConcatenateVideosAPIView.as_view(), name='concatenate-videos'),
]
