# data/__init__.py

"""
Data package for the Automated Traffic & Lane Detection project.
Contains test videos, sample images, and datasets.
"""

import os

def get_video_path(filename: str = "test_video_compressed.mp4") -> str:
    """
    Returns the absolute path to a video file in the data directory.
    Validates that the file exists and is a supported video format.
    
    Args:
        filename (str): The name of the video file. Defaults to "test_video.mp4".
        
    Returns:
        str: Absolute path to the video file.
        
    Raises:
        FileNotFoundError: If the video file does not exist.
        ValueError: If the file is not a supported video format.
    """
    # Get the directory of the current file (the 'data' folder)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(base_dir, filename)
    
    # 1. Check if file exists
    if not os.path.exists(video_path):
        raise FileNotFoundError(
            f"Video file not found at: {video_path}\n"
            f"Please download a dashcam video and place it in the 'data/' folder as '{filename}'."
        )
        
    # 2. Check if it's a supported video format (MP4, AVI, MOV)
    valid_extensions = ('.mp4', '.avi', '.mov', '.mkv')
    if not video_path.lower().endswith(valid_extensions):
        raise ValueError(
            f"Unsupported video format: {filename}\n"
            f"Supported formats: {', '.join(valid_extensions)}"
        )
        
    return video_path
