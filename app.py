import os
import streamlit as st
from main import extract_title, split_pdf
from zipfile import ZipFile
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

        # Save the uploaded file with the original name
        original_file_name = uploaded_file.name
        uploaded_file_path = os.path.join(tempfile.gettempdir(), original_file_name)
        with open(uploaded_file_path, "wb") as file:
            file.write(uploaded_file.getvalue())

        intervals_input = st.text_input("Enter the number of pages per file (optional):")
        start_page_input = st.text_input("Enter the start page for title extraction (optional):")
        start_line_input = st.text_input("Enter the start line on the selected page for title extraction (optional):")

        if st.button("Split"):
            intervals = int(intervals_input) if intervals_input else 1
            start_page = int(start_page_input) if start_page_input else None
            start_line = int(start_line_input) if start_line_input else None

            split_pdf(uploaded_file_path, intervals, start_page, start_line)

            st.write("PDF splitting complete.")

            # Display the split PDF files
            file_names = []

            if start_page is None:
                file_names = [file for file in os.listdir() if file.startswith("split_") and file.endswith(".pdf")]
            else:
                with open(uploaded_file_path, "rb") as file:
                    pdf_file_path = file.read()
                    file.seek(0)
                    file_names = []
                    split_pdf(file, intervals, start_page, start_line)
                    for i in range(start_page, start_page + intervals):
                        title = extract_title(pdf_file_path, i, start_line)
                        if title:
                            title = title.replace(" ", "_")
                            file_name = f"split_{original_file_name}_{title}.pdf"
                            file_names.append(file_name)

            if file_names:
                st.write("Split files:")
                for file_name in file_names:
                    st.write(file_name)

                # Create a zip file containing the split files
                with tempfile.TemporaryDirectory() as temp_dir:
                    zip_file_path = os.path.join(temp_dir, "split_files.zip")
                    with ZipFile(zip_file_path, "w") as zip:
                        for file_name in file_names:
                            zip.write(file_name)

                    # Provide a download button for the zip file
                    st.download_button("Download all files", data=open(zip_file_path, "rb"), file_name="split_files.zip")
            else:
                st.write("No files were split.")


if __name__ == "__main__":
    main()
