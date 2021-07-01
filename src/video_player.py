"""A video player class."""

from .video_library import VideoLibrary
from random import randint
from .video_playlist import Playlist

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video = ''
        self.pause = False
        self._playlists = {}
    
        

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        video_lst = self._video_library.get_all_videos()    # get list of video objects
        
        video_lst = sorted(video_lst, key=lambda x: x.title)
        print('Here\'s a list of all available videos:')
        for vid in video_lst:
            print(vid.video_info)
            
            
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        
        vid = self._video_library.get_video(video_id)
        if not vid in self._video_library.get_all_videos():
            print("Cannot play video: Video does not exist")
            return
        elif vid.is_flagged == True:
            print("Cannot play video: Video is currently flagged", vid.flag_explanation)
            return
        
        title = vid.title
        
        if self.current_video == '':
            pass
        else:
            self.stop_video()
        
        print("Playing video: " + title)
            
        self.current_video = vid
        self.pause = False
    
            
        
        

    def stop_video(self):
        """Stops the current video."""
        if self.current_video == '':
            print("Cannot stop video: No video is currently playing")
        else:
            title = self.current_video.title            
            print("Stopping video: " + title)
            self.current_video = ''
            self.pause = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        
        unflagged_video_lst = [vid for vid in self._video_library.get_all_videos() if vid.is_flagged == False]
        n = len(unflagged_video_lst)
        
        if n==0:
            print("No videos available")
            return
        i = randint(0,n-1)
            
        self.play_video(self._video_library.get_all_videos()[i].video_id)
        
        

    def pause_video(self):
        """Pauses the current video."""
        if self.current_video == '':
            print("Cannot pause video: No video is currently playing")
            return
        if self.pause == True:
            print("Video already paused: " + self.current_video.title)
        else:
            print("Pausing video: " + self.current_video.title)
            self.pause = True
        
       

    def continue_video(self):
        """Resumes playing the current video."""
        if self.current_video == '':
            print("Cannot continue video: No video is currently playing")
            return
        if self.pause == False:
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video: " + self.current_video.title)
            

       

    def show_playing(self):
        """Displays video currently playing."""
        if self.current_video == '':
            print("No video is currently playing")
            return
        pause_status = ''
        if self.pause == True:
            pause_status = "- PAUSED"
        print("Currently playing:" + self.current_video.video_info, pause_status) 
        

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        internal_playlist_name = playlist_name.lower()  # Internal playlist name used for all commands
        if internal_playlist_name in self._playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
            return
            
        self._playlists[internal_playlist_name] = Playlist(playlist_name)   # First argument is original playlist name, second is video list
        print("Successfully created new playlist:", playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        internal_playlist_name = playlist_name.lower()
        if not internal_playlist_name in self._playlists:
            print("Cannot add video to", playlist_name + ": Playlist does not exist")
            return
        vid = self._video_library.get_video(video_id)
        if vid == None:
            print("Cannot add video to", playlist_name + ": Video does not exist")
            return
        elif vid.is_flagged == True:
            print("Cannot add video to", playlist_name +": Video is currently flagged", vid.flag_explanation)
        elif vid in self._playlists[internal_playlist_name].get_videos():
            print("Cannot add video to", playlist_name + ": Video already added")
            return
        else:
           self._playlists[internal_playlist_name].add_video(vid)
           print("Added video to", playlist_name + ":", vid.title)
           
        

    def show_all_playlists(self):
        """Display all playlists."""
        if not self._playlists:
            print("No playlists exist yet")
        else:
            playlist_lst = [pl.original_name for pl in self._playlists.values()]
            playlist_lst.sort()
            print("Showing all playlists:")
            for p in playlist_lst:
                print(p)
        
        
        

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        internal_playlist_name = playlist_name.lower()
        if not internal_playlist_name in self._playlists:
            print("Cannot show playlist", playlist_name + ": Playlist does not exist")
            return
        
        print("Showing playlist:", playlist_name)
        if not self._playlists[internal_playlist_name].get_videos():
            print(" No videos here yet")
        else:
            for vid in self._playlists[internal_playlist_name].get_videos():
                print(vid.video_info)
            
        

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        internal_playlist_name = playlist_name.lower()
        if not internal_playlist_name in self._playlists:
            print("Cannot remove video from", playlist_name + ": Playlist does not exist")
            return
        vid = self._video_library.get_video(video_id)
        if vid == None:
            print("Cannot remove video from", playlist_name + ": Video does not exist")
            return
        elif not vid in self._playlists[internal_playlist_name].get_videos():
            print("Cannot remove video from", playlist_name + ": Video is not in playlist")
            return
        else:
           self._playlists[internal_playlist_name].remove_video(vid)
           print("Removed video from", playlist_name + ":", vid.title)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        internal_playlist_name = playlist_name.lower()
        if not internal_playlist_name in self._playlists:
            print("Cannot clear playlist", playlist_name + ": Playlist does not exist")
            return
        else:
            self._playlists[internal_playlist_name].clear_playlist()
            print("Successfully removed all videos from", playlist_name)
        

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        internal_playlist_name = playlist_name.lower()
        if not internal_playlist_name in self._playlists:
            print("Cannot delete playlist", playlist_name + ": Playlist does not exist")
            return
        else:
            del self._playlists[internal_playlist_name]
            print("Deleted playlist:", playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        relevant_vids = []
        for vid in self._video_library.get_all_videos():
            if vid.is_flagged==False:
                if search_term.lower() in vid.title.lower():
                    relevant_vids.append(vid)
        
        if not relevant_vids:
            print("No search results for", search_term)
        else:
            relevant_vids = sorted(relevant_vids, key = lambda x: x.title)
            
            print("Here are the results for", search_term + ":")
            i = 1
            for vid in relevant_vids:
                print(" " + str(i) + ")" + vid.video_info)
                i+=1
            print("Would you like to play any of the above? If yes, specify the number of the video. \n If your answer is not a valid number, we will assume it's a no.")
            
            
            
            index = input()
            
            try:
                j = int(index)-1
                vid = relevant_vids[j]
                self.play_video(vid.video_id)
            except (ValueError, IndexError):
                pass

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        relevant_vids = []
        
        for vid in self._video_library.get_all_videos():
            if vid.is_flagged==False:
                tag_lst = list(vid.tags)
                tag_lst = [w.lower() for w in tag_lst]
                if video_tag.lower() in tag_lst:
                    relevant_vids.append(vid)
        
        if not relevant_vids:
            print("No search results for", video_tag)
        else:
            relevant_vids = sorted(relevant_vids, key = lambda x: x.title)
            
            print("Here are the results for", video_tag + ":")
            i = 1
            for vid in relevant_vids:
                print(" " + str(i) + ")" + vid.video_info)
                i+=1
            print("Would you like to play any of the above? If yes, specify the number of the video. \n If your answer is not a valid number, we will assume it's a no.")
            
            
            
            index = input()
            
            
            index = input("Would you like to play any of the above? If yes, specify the number of the video. \n If your answer is not a valid number, we eill assume it's a no.")
            
            try:
                j = int(index)-1
                vid = relevant_vids[j]
                self.play_video(vid.video_id)
            except (ValueError, IndexError):
                pass

    def flag_video(self, video_id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video. If not provided, 'Not supplied' will be displayed.
        """
        vid = self._video_library.get_video(video_id)
        if vid == None:
            print("Cannot flag video: Video does not exist")
            
        elif vid.is_flagged == True:
            print("Cannot flag video: Video is already flagged")
        else:
            vid.flag(flag_reason)
            if self.current_video == '':
                pass
            elif self.current_video.video_id == video_id:
                self.stop_video()
            print("Successfully flagged video:", vid.title, vid.flag_explanation)
            
          
            

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        vid = self._video_library.get_video(video_id)
        if vid == None:
            print("Cannot remove flag from video: Video does not exist")
        elif vid.is_flagged == False:
            print("Cannot remove flag from video: Video is not flagged")
        else:
            vid.unflag()
            print("Successfully removed flag from video:", vid.title)
