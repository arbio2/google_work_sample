"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)        
        
        # Create a variable to track whether the video is flagged
        # and the reason for this if one was given
        self._flagged = False
        self._flag_reason = ""
        
    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags
    
    @property
    def is_flagged(self) -> bool:
        return self._flagged
    
    def flag(self, flag_reason = "Not supplied"):
        self._flagged = True
        self._flag_reason = flag_reason
    
    def unflag(self):
        self._flagged = False
        self._flag_reason = ""
        
    @property
    def flag_explanation(self) -> str:
        expl = "(reason: " + self._flag_reason + ")"
        return expl
        
    
    @property
    def video_info(self) -> str:
        """
        Returns the list of tags in a string format useful for the functions of video_player module
        The tests require a specific format in the output which is repeated in several functions, so it is useful
        to define this property here
        """
        
        # a string that transforms the tags into the format required by the tests
        t_str = ''
        if self._tags:
            for tag in list(self._tags):
                t_str += (tag + " ")
            t_str = "[" + t_str[:-1] + "]"
        else:
            t_str = "[]"
        
        # a string that is non-empty if the video is flagged
        flag_str = ''
        if self.is_flagged==True:
            flag_str = " - FLAGGED " + self.flag_explanation
            
        # combining all the details of the video into the required format
        info = ' ' + self.title + " ("+self.video_id+")" + " " + t_str + flag_str
        return info
        
           