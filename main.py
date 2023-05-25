import os
from math import ceil
from PyPDF2 import PdfReader, PdfWriter


def extract_title(page, line):
    """
    Extracts the text of a specific line from a page.

    Args:
        page: Page object from PyPDF2 representing the page to extract the title from.
        line: Line number to extract the text from.

    Returns:
        The extracted text of the specified line, or None if the line is out of range.
    """
    extracted_text = page.extract_text()
    lines = extracted_text.split('\n')
    if line and line <= len(lines):
        return lines[line - 1].strip()
    else:
        return None


def split_pdf(input_file, num_intervals=1, start_page=None, start_line=None):
    """
    Splits a PDF file into multiple smaller files based on the specified number of intervals.

    Args:
        input_file: Path to the input PDF file.
        num_intervals: Number of pages per file (default is 1).
        start_page: Start page for title extraction (optional).
        start_line: Start line on the selected page for title extraction (optional).
    """
    with open(input_file, 'rb') as file:
        pdf_reader = PdfReader(file)
        total_pages = len(pdf_reader.pages)

        pages_per_interval = num_intervals

        interval_num = 1
        start_index = 0

        while start_index < total_pages:
            end_index = min(start_index + pages_per_interval, total_pages) - 1

            pdf_writer = PdfWriter()

            # Add pages to the PdfWriter object for the current interval
            for page_index in range(start_index, end_index + 1):
                page = pdf_reader.pages[page_index]
                pdf_writer.add_page(page)

            title = extract_title(pdf_writer.pages[0], start_line)

            # Check if title is None or empty, set default title if necessary
            if not title:
                title = f"split_{os.path.splitext(os.path.basename(input_file))[0]}"

            output_file = f"{title}_{interval_num}.pdf"
            with open(output_file, 'wb') as output:
                pdf_writer.write(output)

            print(f"Split PDF {interval_num} saved as {output_file}")

            interval_num += 1
            start_index = end_index + 1
