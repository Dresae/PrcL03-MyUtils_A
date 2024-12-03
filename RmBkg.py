from PIL import Image
# built-in package sys
import sys

# Ensure to customize the input and output paths
input_path = 'X:/Directory/Path/Picture.png'
output_path = 'X:/Directory/Path/Picture_processed.png'

def remove_white_background(input_path, output_path):
    # Open the input image
    img = Image.open(input_path).convert("RGBA")
    
    # Create a new image with the same size and a transparent background
    new_img = Image.new("RGBA", img.size)

    total_pixels = img.width * img.height
    processed_pixels = 0

    # Iterate over each pixel in the image
    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = img.getpixel((x, y))
            # Check if the pixel is white (or close to white)
            if r > 200 and g > 200 and b > 200:
                # Make it transparent
                new_img.putpixel((x, y), (r, g, b, 0))
            else:
                # Keep the original pixel
                new_img.putpixel((x, y), (r, g, b, a))
            
            # Update progress
            processed_pixels += 1
            print_progress(processed_pixels, total_pixels)

    # Save the new image
    new_img.save(output_path)

def print_progress(processed, total):
    """Prints the progress of the operation in the terminal."""
    percent = (processed / total) * 100
    bar_length = 40  # Length of the progress bar
    block = int(round(bar_length * percent / 100))
    progress_bar = '#' * block + '-' * (bar_length - block)
    sys.stdout.write(f'\r|{progress_bar}| {percent:.2f}%')
    sys.stdout.flush()

#print(print_progress)  # To move to the next line after the progress bar completes