import os
from PIL import Image, ExifTags
import shutil

def resize_images_in_folder(folder_path):
    # Set the desired size
    new_size = (600, 600)
    max_file_size = 50 * 1024  # 240 KB

    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # List all files in the folder
    files = os.listdir(folder_path)

    # Initialize a counter to track the number of images resized
    num_resized = 0

    # Initialize a counter to track the number of oversized images
    num_oversized = 0

    # Create a temporary folder to hold resized images
    temp_folder = os.path.join(folder_path, 'temp_resized')
    os.makedirs(temp_folder, exist_ok=True)

    # Loop through each file in the folder
    for filename in files:
        # Check if the file is an image (you can add more extensions as needed)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            try:
                # Open the image
                with Image.open(os.path.join(folder_path, filename)) as img:
                    # Check for and adjust orientation
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation] == 'Orientation':
                            break
                    exif = dict(img._getexif().items())
                    if orientation in exif:
                        if exif[orientation] == 3:
                            img = img.rotate(180, expand=True)
                        elif exif[orientation] == 6:
                            img = img.rotate(270, expand=True)
                        elif exif[orientation] == 8:
                            img = img.rotate(90, expand=True)

                    # Resize the image with LANCZOS filter (alternative to ANTIALIAS)
                    img = img.resize(new_size, Image.LANCZOS)
                    
                    # Save the resized image with the same filename to the temporary folder
                    temp_filepath = os.path.join(temp_folder, filename)
                    img.save(temp_filepath)
                    
                    # Check the size of the resized image
                    if os.path.getsize(temp_filepath) <= max_file_size:
                        # Replace the original image with the resized one
                        shutil.move(temp_filepath, os.path.join(folder_path, filename))
                        num_resized += 1
                    else:
                        # Rename the oversized image
                        base_filename, file_extension = os.path.splitext(filename)
                        oversized_filename = f"{base_filename}_OVERSIZE{file_extension}"
                        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, oversized_filename))
                        num_oversized += 1
            except Exception as e:
                print(f"Error processing '{filename}': {e}")

    # Remove the temporary folder
    shutil.rmtree(temp_folder)

    if num_resized > 0:
        print(f"{num_resized} image(s) resized successfully.")
    else:
        print("No images were resized.")
    
    if num_oversized > 0:
        print(f"{num_oversized} image(s) were renamed as 'OVERSIZE'.")
    
    if num_oversized == 0 and num_resized == 0:
        print("No images found for processing.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing the images: ").strip()
    resize_images_in_folder(folder_path)
    input("Press Enter to exit.")
