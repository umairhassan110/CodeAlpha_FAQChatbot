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




