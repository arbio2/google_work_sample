"""A video playlist class."""
from .video import Video
from .video_library import VideoLibrary

class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, name):
        self._video_library = VideoLibrary()
        self._original_name = name
        self._internal_name = name.lower()
        self._videos = []
    
    @property
    def original_name(self) -> str:
        return self._original_name
        
    @property
    def internal_name(self) -> str:
        return self._internal_name
    
    
    def get_videos(self):
        return self._videos
    
    def add_video(self, vid):
        self._videos.append(vid)
    
    def remove_video(self, vid):
        self._videos.remove(vid)
        
    def clear_playlist(self):
        self._videos.clear()    