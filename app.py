import os
import streamlit as st
from main import extract_title, split_pdf
import tempfile

def main():
    # Streamlit app
    st.title("PDF Splitting Tool")

    # File upload
    uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_file_path = tmp.name

            intervals_input = st.text_input("Enter the number of pages per file (optional):")
            start_page_input = st.text_input("Enter the start page for title extraction (optional):")
            start_line_input = st.text_input("Enter the start line on the selected page for title extraction (optional):")

            if st.button("Split"):
                intervals = int(intervals_input) if intervals_input else 1
                start_page = int(start_page_input) if start_page_input else None
                start_line = int(start_line_input) if start_line_input else None
