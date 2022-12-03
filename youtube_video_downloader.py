"""
=========================
YouTube Video Downloader
=========================

Required Packages:
- pytube
"""

# ! pip install pytube


# Importing the Libraries
# Standard libs
import os.path
from os import path
from IPython.display import Image
# Packages
from pytube import YouTube


# Making a Directory
Path = '/YouTubeVideoDownloder_Output'

if path.exists(Path) == False:
  os.mkdir(Path)

os.chdir(Path)
# print("Working directory:")
# !pwd
# !ls



def download(video_resolutions, videos):
    while True:
        # Looping through the video_resolutions list to be displayed on the screen for user selection...
        i = 1
        for resolution in video_resolutions:
            print(f'{i}. {resolution}')
            i += 1

        # To Download the video with the users Choice of resolution
        choice = int(input('\nChoose A Resolution Please: '))
        
        # To validate if the user enters a number displayed on the screen...
        if 1 <= choice < i:
            resolution_to_download = video_resolutions[choice - 1]
            print(f"You're now downloading the video with resolution {resolution_to_download}...")

            # command for downloading the video
            videos[choice - 1].download()

            print("\nVideo was successfully downloaded!")
            break

        else:
            print("Invalid choice!!\n\n")


def sort_resolutions(url):
    # URL (user input)
    try:
      my_video = YouTube(url)
      print("\nTitle of The Video:")
      print(my_video.title)

      # Now for the Thumbnail Image
      print("Thumbnail URL:")
      print(my_video.thumbnail_url)

      video_resolutions = []
      videos = []

      for stream in my_video.streams.filter(progressive=True).order_by('resolution'):
          # print(stream)
          video_resolutions.append(stream.resolution)
          videos.append(stream)

      # print(video_resolutions)
      return video_resolutions, videos

    except:
      print(f'Video {url} is unavaialable')
      


url = input('Please input the URL : ')

video_resolutions, videos = sort_resolutions(url)

download(video_resolutions, videos)