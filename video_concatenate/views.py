from django.shortcuts import render
from video_concatenate.tasks import concatenate_videos

def concatenate_view(request):
    # Example file paths (you can get these from the uploaded files)
    video1_path = "/home/dci-student/P24-E04/PROJECT IDEAS/video_enhancement_tools/video1_path.mp4"
    video2_path = "/home/dci-student/P24-E04/PROJECT IDEAS/video_enhancement_tools/video2_path.mp4"
    joined_video_path = "/home/dci-student/P24-E04/PROJECT IDEAS/video_enhancement_tools/joined_video.mp4"
    
    # Trigger the Celery task
    concatenate_videos.apply_async(
        args=[video1_path, video2_path, joined_video_path]
    )

    return render(request, "concatenate_result.html", {"message": "Video concatenation in progress!"})

