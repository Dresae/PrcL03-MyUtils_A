"""
Title: Remove Background
Description: This script removes the white background from an image using a simplistic GUI.
Contributor: Dresae
"""

from rembg import remove
import easygui
from PIL import Image

input_path = easygui.fileopenbox(title='Select image file')
output_path = easygui.filesavebox(title='Save file to...')

def edit_pic():
    input = Image.open(input_path)
    output =remove(input)
    # img_resized = output.resize((500, 500)) * Modify parameter to scale up or down
    output.save(output_path)

edit_pic()