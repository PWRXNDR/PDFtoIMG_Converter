import fitz  # PyMuPDF
import os

def pdf_to_img(working_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # List all PDF files in the working directory
    pdf_files = [file for file in os.listdir(working_dir) if file.endswith('.pdf')]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(working_dir, pdf_file)
        pdf_document = fitz.open(pdf_path)

        # Assuming single-page PDFs, extract the first (and only) page
        page = pdf_document.load_page(0)
        image = page.get_pixmap()
        image.save(os.path.join(output_dir, f'{os.path.splitext(pdf_file)[0]}.png'), 'png')

        pdf_document.close()

# Ask user for the input and output directory paths
input_dir = input("Enter the input directory path: ")
output_dir = input("Enter the output directory path: ")

pdf_to_img(input_dir, output_dir)
