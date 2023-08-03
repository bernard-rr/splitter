# Splitter - Keep Your Data Private

[Splitter](https://splitter.streamlit.app/)


## Overview

The Splitter is a simple yet powerful web application that allows you to split large PDF files into smaller files based on the specified number of intervals. The tool is designed to help you manage your PDF documents efficiently, and it ensures that your sensitive data remains private as all the operations are performed locally on your device.

## Features

- **Split PDF Files:** Upload a PDF file, and the tool will split it into smaller files based on the specified number of pages per file.
- **Title Extraction:** Optionally, you can provide a start page and line number to extract text and use it as the title for the split files.
- **Download ZIP Archive:** The split files are compressed into a ZIP archive for easy downloading.
- **Privacy Assured:** All the processing happens locally on your device; no data is sent to any external server.

## How to Use

1. **Upload PDF File:** Drag and drop your PDF file or click the "Upload PDF file" button to select the file from your computer.
2. **Split Configuration:** Optionally, you can set the number of pages per split file, start page, and start line for title extraction. The default values are 1 page per file and no title extraction.
3. **Click "Split":** After configuring your settings, click the "Split" button to start the process.
4. **Download Results:** Once the splitting is complete, you will see the split files listed below. You can download all the files as a ZIP archive for easy storage and sharing.

## Requirements

- Python 3.7 or later
- Streamlit
- PyPDF2

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/yourusername/your-repo.git
```

2. Install the required dependencies:

```
pip install streamlit PyPDF2
```

3. Run the Streamlit app:

```
streamlit run app.py
```

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact

For any questions or inquiries, feel free to contact us at [bernardchidi5@gmail.com](mailto:bernardchidi5@gmail.com).
