# from pypdf import PdfReader, PdfWriter
# from pathlib import Path
#
# # Define the folder path
# folder_path = Path(r"C:\Users\saswa\Desktop\Python\Exercise-8")
#
# # Get a list of all PDF files in the folder
# pdf_files = [file for file in folder_path.glob("*.pdf")]
#
# # Create a PdfWriter object
# writer = PdfWriter()
#
# # Append each PDF file to the writer
# for pdf_file in pdf_files:
#     # Read the PDF file
#     reader = PdfReader(pdf_file)
#     # Add each page of the PDF to the writer
#     for page in reader.pages:
#         writer.add_page(page)
#
# # Write out the merged PDF
# with open("mergedPdf.pdf", "wb") as output_pdf:
#     writer.write(output_pdf)
#
#
# #as
# # C:\Users\saswa\PycharmProjects\pythonProject\.venv\Scripts\python.exe "C:\Users\saswa\PycharmProjects\pythonProject\Video-76-Exercise 8 - Merge the PDF.py"
# # C:\Users\saswa\PycharmProjects\pythonProject\Video-76-Exercise 8 - Merge the PDF.py:11: DeprecationWarning: PdfMerger is deprecated and will be removed in pypdf 5.0.0. Use PdfWriter instead.
# #   merger = PdfMerger()
# #
# # Process finished with exit code 0
#
# #The issue is that the PdfWriter.add_page() method expects a page object, not a file path. The correct approach involves reading the PDF file using PdfReader and then adding each page to PdfWriter.

from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]  # this line can be manipulated to merge the pdfs in different ways

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

# # Get the current working directory
# current_directory = os.getcwd()
#
# # Print the current working directory
# print(f"Current directory: {current_directory}")