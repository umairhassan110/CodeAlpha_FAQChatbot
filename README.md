# FAQ Chatbot

An intelligent FAQ chatbot built with Python and Streamlit that answers technology related questions using Natural Language Processing and Cosine Similarity.

## Features

- Answers frequently asked questions about technology
- Uses NLP techniques for text preprocessing
- Cosine Similarity for finding best matching answers
- Interactive chat interface
- Handles unrecognized questions gracefully

## Technologies Used

- Python 3.x
- Streamlit
- Scikit-learn
- NLTK Natural Language Toolkit

## Installation

1. Clone the repository

2. Navigate to project directory
cd CodeAlpha_FAQChatbot

3. Install required libraries
pip install streamlit scikit-learn nltk

## Usage

Run the application using the following command:
streamlit run app.py

Then open your browser and go to:
http://localhost:8501

## How It Works

1. User enters a question in the chat interface
2. The question is cleaned and preprocessed using NLTK
3. TF-IDF Vectorization converts text into numerical form
4. Cosine Similarity finds the most similar FAQ
5. The best matching answer is displayed to the user

## Topics Covered

- Python Programming
- Artificial Intelligence
- Machine Learning
- Deep Learning
- Neural Networks
- Data Science
- Cloud Computing
- Cybersecurity
- Blockchain
- Internet of Things

## Project Structure
CodeAlpha_FAQChatbot/
app.py
README.md

## Internship

This project was developed as part of the CodeAlpha Artificial Intelligence Internship Program.

README 3 — Object Detection
CodeAlpha_ObjectDetection folder mein README.md naam se banao:
markdown# Object Detection and Tracking

A real time object detection and tracking application built with Python, OpenCV and YOLOv11 that detects and tracks multiple objects through a webcam feed.

## Features

- Real time object detection using YOLOv11
- Object tracking with unique tracking IDs
- Supports detection of 80 different object classes
- Bounding boxes with labels drawn on each frame
- Webcam support
- Press Q to quit the application

## Technologies Used

- Python 3.x
- OpenCV
- Ultralytics YOLOv11

## Installation

1. Clone the repository
git clone https:https://github.com/umairhassan110/CodeAlpha_FAQChatbot

2. Navigate to project directory
cd CodeAlpha_ObjectDetection

3. Install required libraries
pip install opencv-python ultralytics

## Usage

Run the application using the following command:
python app.py

The webcam will open automatically and start detecting objects in real time.
Press Q to quit the application.

## Detectable Objects

YOLOv11 can detect 80 different objects including:

- Person
- Car
- Motorcycle
- Bus
- Truck
- Laptop
- Phone
- Chair
- Bottle
- And many more

## How It Works

1. Webcam captures video frames in real time
2. Each frame is passed to YOLOv11 model
3. Model detects objects and assigns tracking IDs
4. Bounding boxes and labels are drawn on each frame
5. Processed frame is displayed in a window

