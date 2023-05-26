import streamlit as st
import tempfile
import os
from zipfile import ZipFile
from main import split_pdf, extract_title


def main():
    # Streamlit app
    st.title("PDF Splitting Tool")

    # File upload
    uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])

    if st.button("Refresh"):
            # Manually refresh the page
            st.experimental_rerun()

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
                with tempfile.TemporaryDirectory() as temp_dir:
                    zip_file_path = os.path.join(temp_dir, "split_files.zip")
                    with ZipFile(zip_file_path, "w") as zip:
                        for file_name in file_names:
                            new_name = f"split_{original_file_name}_{file_name}"
                            zip.write(file_name, arcname=new_name)

                    # Provide a download button for the zip file
                    with open(zip_file_path, "rb") as zip_file:
                        st.download_button("Download all files", data=zip_file, file_name="split_files.zip")
            else:
                st.write("No files were split.")

        # Clean up the temporary file
        os.remove(uploaded_file_path)


if __name__ == "__main__":
    main()
