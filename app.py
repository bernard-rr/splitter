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

                split_pdf(tmp_file_path, intervals, start_page, start_line)

                st.write("PDF splitting complete.")

                # Display the split PDF files
                file_names = []

                if start_page is None:
                    file_names = [file for file in os.listdir() if file.startswith("split_") and file.endswith(".pdf")]
                else:
                    for file in os.listdir():
                        if file.endswith(".pdf"):
                            page_number = int(file.split("_")[1].split(".")[0])
                            if page_number >= start_page:
                                file_names.append(file)

                if file_names:
                    st.write("Split files:")
                    for file_name in file_names:
                        st.write(file_name)

                    # Create a zip file containing the split files
                    with ZipFile("split_files.zip", "w") as zip:
                        for file_name in file_names:
                            zip.write(file_name)

                    # Provide a download link for the zip file
                    st.markdown("[Download all files](split_files.zip)")
                else:
                    st.write("No files were split.")


if __name__ == "__main__":
    main()