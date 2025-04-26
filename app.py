# app.py

import streamlit as st
from review_summarizer import summarizer_workflow
from chatbot_generator import chatbot_workflow

from sentiment_analyzer import sentiment_workflow
from marketing_copy_generator import marketing_workflow

st.set_page_config(page_title="AutoCommerce Suite", layout="wide")

st.title("🚀 AutoCommerce Suite")
st.sidebar.title("Select a Feature")

option = st.sidebar.selectbox(
    "Choose a functionality:",
    (
        "Chatbot Generator from FAQ",
        "Product Review Summarizer",
        "Customer Sentiment Analyzer",
        "Marketing Copy Generator"
    )
)

if option == "Chatbot Generator from FAQ":
    chatbot_workflow()
elif option == "Product Review Summarizer":
    summarizer_workflow()
elif option == "Customer Sentiment Analyzer":
    sentiment_workflow()
elif option == "Marketing Copy Generator":
    marketing_workflow()
