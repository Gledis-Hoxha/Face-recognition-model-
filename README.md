# Face Recognition Model

This project is a school collaboration focused on building a face recognition system using Python. It was developed as part of an academic workshop to explore computer vision concepts and real-time identity detection.

## Overview

The system uses machine learning techniques to detect and recognize faces from either static images or a live webcam feed. It is capable of identifying known individuals based on a training dataset.

## Features

- Detects faces using OpenCV or similar tools
- Recognizes individuals using a trained model
- Supports live camera input or image folder input
- Includes dataset creation and labeling
- Can be extended with attendance logging or access control systems

## Technologies Used

- Python
- OpenCV
- face_recognition (dlib-based)
- NumPy
- (Optional) Flask for interface or API (if applicable)

## Installation

```bash
# Clone the repository
git clone https://github.com/Gledis-Hoxha/Face-recognition-model-.git
cd Face-recognition-model-

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the main script
python face_recognition_main.py  # Replace with actual script name
