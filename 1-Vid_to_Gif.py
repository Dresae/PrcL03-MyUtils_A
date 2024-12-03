"""
Title: 
Description: This script converts a video file to GIF animation using a simplistic GUI.
Contributor: Dresae
"""

from moviepy.editor import VideoFileClip
import easygui

input_path = easygui.fileopenbox(title='Select video file')
output_path = easygui.filesavebox(title='Save GIF to...')

# Load the video
videoclip = VideoFileClip(input_path)

# Trim the video 
videoclip = videoclip.subclip(4, 12)

# Write the GIF
videoclip.write_gif(output_path)