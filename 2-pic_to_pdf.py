"""
Title: Picture to PDF converter
Description: This script converts a picture file to PDF using a simplistic GUI.
Contributor: Dresae
"""
from PIL import Image # Pillow package must be installed
from reportlab.pdfgen import canvas
import easygui

input_path = easygui.fileopenbox(title='Select video file')
output_path = easygui.filesavebox(title='Save GIF to...')

def png_to_pdf(png_file, pdf_file):
	
	image = Image.open(png_file)        # Open the PNG file

	c = canvas.Canvas(pdf_file)         # Create a PDF canvas# Create a PDF canvas

	width, height = image.size          # Get image dimensions
	
	c.setPageSize(width, height)        # Set the page size to match the image size

	c.drawImage(png_file, 0, 0, width, height)  # Draw the image on the PDF canvas

	
	c.save()                            # Save the PDF file 

png_to_pdf(input_path, output_path)# Convert the PNG file to PDF