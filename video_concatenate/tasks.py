from celery import shared_task
from moviepy import VideoFileClip, concatenate_videoclips
import os

@shared_task
def concatenate_videos(video1, video2, joined_video_path):
    try:
        clip1 = VideoFileClip(video1)
        clip2 = VideoFileClip(video2)
        final_clip = concatenate_videoclips([clip1, clip2])
        final_clip.write_videofile(joined_video_path, codec="libx264", fps=24)
        return f"Video successfully saved as {joined_video_path}"
    except Exception as e:
        return str(e)


