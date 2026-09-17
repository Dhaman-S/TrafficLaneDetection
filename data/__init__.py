# data/__init__.py

"""
Data package for the Automated Traffic & Lane Detection project.
Contains test videos, sample images, and datasets.
"""

import os

def get_video_path(filename: str = "test_video.mp4") -> str:
    """
    Returns the absolute path to a video file in the data directory.
    
    Args:
        filename (str): The name of the video file. Defaults to "test_video.mp4".
        
    Returns:
        str: Absolute path to the video file.
    """
    # Get the directory of the current file (the 'data' folder)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, filename)

def get_image_path(filename: str) -> str:
    """Returns the absolute path to an image file in the data directory."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, filename)
