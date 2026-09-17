# src/__init__.py

"""
Automated Traffic & Lane Detection Package.
This package contains modules for preprocessing, lane detection, 
traffic detection, and visualization.
"""

__version__ = "1.0.0"

from .preprocessor import Preprocessor
from .lane_detector import LaneDetector
from .traffic_detector import TrafficDetector
from .visualizer import Visualizer

__all__ = [
    'Preprocessor',
    'LaneDetector',
    'TrafficDetector',
    'Visualizer'
]
