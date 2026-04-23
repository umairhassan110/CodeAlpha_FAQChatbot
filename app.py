faqs = [
    {
        "question": "What is Python?",
        "answer": "Python is a high-level, easy-to-learn programming language used for web development, AI, data science, and automation."
    },
    {
        "question": "What is Artificial Intelligence?",
        "answer": "Artificial Intelligence (AI) is the simulation of human intelligence by machines to perform tasks like learning, problem-solving, and decision-making."
    },
    {
        "question": "What is Machine Learning?",
        "answer": "Machine Learning is a subset of AI where machines learn from data to make predictions or decisions without being explicitly programmed."
    },
    {
        "question": "What is Deep Learning?",
        "answer": "Deep Learning is a subset of Machine Learning that uses neural networks with many layers to analyze large amounts of data."
    },
    {
        "question": "What is a neural network?",
        "answer": "A neural network is a series of algorithms that mimic the human brain to recognize patterns and solve complex problems."
    },
    {
        "question": "What is Data Science?",
        "answer": "Data Science is a field that uses statistics, programming, and machine learning to extract insights and knowledge from data."
    },
    {
        "question": "What is Cloud Computing?",
        "answer": "Cloud Computing is the delivery of computing services like storage, servers, and software over the internet instead of local hardware."
    },
    {
        "question": "What is Cybersecurity?",
        "answer": "Cybersecurity is the practice of protecting computer systems, networks, and data from digital attacks and unauthorized access."
    },
    {
        "question": "What is Blockchain?",
        "answer": "Blockchain is a decentralized digital ledger that records transactions across many computers securely and transparently."
    },
    {
        "question": "What is the Internet of Things?",
        "answer": "IoT refers to physical devices connected to the internet that collect and share data, like smart home devices and wearables."
    }
]

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import string

# Download NLTK data
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

# Page Setup
st.set_page_config(page_title="Tech FAQ Chatbot")
st.title("Technology FAQ Chatbot")
st.markdown("Ask me anything about Technology, AI, Python & more!")

# Text Cleaning Function
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# Find Best Match Function
def get_best_match(user_question):
    # Clean all questions
    all_questions = [clean_text(faq["question"]) for faq in faqs]
    cleaned_user_q = clean_text(user_question)
    
    # Add user question to list
    all_questions.append(cleaned_user_q)
    
    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_questions)
    
    # Cosine Similarity
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    best_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_index]
    
    return best_index, best_score

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if user_input := st.chat_input("Ask your technology question here..."):
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get best match
    best_index, best_score = get_best_match(user_input)

    # Generate Response
    if best_score > 0.2:
        response = f"**Q: {faqs[best_index]['question']}**\n\n{faqs[best_index]['answer']}"
    else:
        response = "Sorry, I couldn't find a relevant answer. Please try rephrasing your question!"

    # Show bot response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")


