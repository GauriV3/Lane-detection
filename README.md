# Lane-detection
**Description:**

This project implements lane detection algorithms in Python using OpenCV and other libraries. It includes two functionalities:

Image Lane Detection: This script processes a single image and detects lane lines within it.
Video Lane Detection: This script processes a video stream and detects lane lines in real-time, overlaying them on the video frames.
Features:

Utilizes OpenCV library for image processing and computer vision tasks.
Employs edge detection and line fitting techniques to identify lane markings.
Provides basic functionalities for lane detection in both images and videos.

**How to Use:**

**1. Image Lane Detection:**

Save the script as image_lane_detection.py.
Place the image you want to process in the same folder as the script (e.g., "2022-02-20_23h29_24.jpg").
Run the script from your terminal using python image_lane_detection.py.
The script will display the processed image with detected lane lines.

**2. Video Lane Detection:**

Save the script as video_lane_detection.py.
Ensure you have a video file named "laneline.jpeg" in the same folder.
(Optional) Replace "laneline.jpeg" with the path to your desired video file.
Run the script from your terminal using python video_lane_detection.py.
The script will process the video and display the output with detected lane lines overlaid on the frames.
Dependencies:

**This project requires the following Python libraries:**

OpenCV
matplotlib
numpy
You can install them using the command pip install opencv-python matplotlib numpy.

**Additional Notes:**

This is a basic implementation of lane detection and can be further improved with more advanced techniques.
Feel free to explore the code and modify it for your specific needs.
