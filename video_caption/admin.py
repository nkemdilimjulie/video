from django.contrib import admin
from .models import VideoWithCaption  # Make sure the model is imported

# Register the model with the admin site
admin.site.register(VideoWithCaption)
