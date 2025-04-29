import os
from PIL import Image

def resize_images_in_folder(folder_path):
    # Set the desired size
    new_size = (1000, 1000)

    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # List all files in the folder
    files = os.listdir(folder_path)

    # Initialize a counter to track the number of images resized
    num_resized = 0

    # Loop through each file in the folder
    for filename in files:
        # Check if the file is an image (you can add more extensions as needed)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            try:
                # Open the image
                with Image.open(os.path.join(folder_path, filename)) as img:
                    # Resize the image with LANCZOS filter (alternative to ANTIALIAS)
                    img = img.resize(new_size, Image.LANCZOS)
                    # Save the resized image with the same filename
                    img.save(os.path.join(folder_path, filename))
                    num_resized += 1
            except Exception as e:
                print(f"Error processing '{filename}': {e}")

    if num_resized > 0:
        print(f"{num_resized} image(s) resized successfully.")
    else:
        print("No images were resized.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing the images: ").strip()
    resize_images_in_folder(folder_path)
    input("Press Enter to exit.")
