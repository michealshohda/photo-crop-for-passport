# Smart Batch Image Cropper

SmartBatchImageCropper is a high-performance Python script designed for media professionals, photographers, and developers who need to crop large batches of portrait images with precise, consistent framing. The script uses facial landmark detection to center the eyes and semi-crop the shoulders, ensuring uniformity across hundreds or thousands of photos within seconds.

## Features

- 📷 **Face Landmark Detection** – Automatically detects key facial features for accurate positioning.
- ⚡ **Batch Processing** – Crops hundreds of images per second using optimized OpenCV routines.
- 🎯 **Consistent Output** – Fixes image dimensions with centered eyes and framed shoulders.
- 🔧 **Configurable** – Easily adjust crop size, face position ratio, and output quality.
- 🏭 **Production Ready** – Originally developed for and used by a media production company.

## Use Case

This tool was created to assist a media production company in automating the tedious and error-prone task of manually cropping large volumes of portraits. It guarantees professional-level consistency and framing with minimal human input.

## Requirements

- Python 3.7+
- OpenCV (`cv2`)
- dlib or mediapipe (depending on your face landmark detector)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/SmartBatchImageCropper.git
   cd SmartBatchImageCropper
