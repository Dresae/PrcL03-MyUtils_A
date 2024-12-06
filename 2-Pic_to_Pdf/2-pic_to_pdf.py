"""
Title: Picture to PDF converter
Description: This script converts a picture file to PDF using a user friendly GUI.
Contributor: Dresae
"""

from tkinter import Tk, Button, filedialog, Label 
from PIL import Image
from fpdf import FPDF

def image_to_pdf(image_path, output_pdf_path):
		# Function to convert image to PDF
		image = Image.open(image_path)
		pdf = FPDF()
		pdf.add_page()
		pdf.image(image_path, x=0, y=0, w=210, h=297)
		pdf.output (output_pdf_path)
		label.config(text=f"{output_pdf_path} created!")

def select_image():
	# Opens the file selection dialog and retrieves the file path
	image_path = filedialog.askopenfilename (title="Select Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]) 
	if image_path:
		output_pdf_path = filedialog.asksaveasfilename (defaultextension=".pdf", title="Save as PDF", filetypes=[("PDF Files", "*.pdf")]) 
		if output_pdf_path:
			image_to_pdf(image_path, output_pdf_path)
			
# Create the Tkinter window and add a button
root = Tk()
root.title("Image to PDF Converter")
root.geometry("300x150")

label = Label(root, text="Image to PDF")
label.pack(pady=10)

button = Button(root, text="Choose Image", command=select_image)
button.pack(pady=10)

root.mainloop()