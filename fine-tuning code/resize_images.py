from PIL import Image
import os

# Folder path for the images
input_folder = '/oid-test/data'
output_folder = '/oid-test/resized-data'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Set target size
target_size = (640, 640)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')):  # Supported formats
        file_path = os.path.join(input_folder, filename)

        # Open an image file
        with Image.open(file_path) as img:
            # Resize the image
            resized_img = img.resize(target_size, Image.LANCZOS)

            # Save resized image to the output folder
            resized_img.save(os.path.join(output_folder, filename))

print(f"All images resized and saved in '{output_folder}'")
