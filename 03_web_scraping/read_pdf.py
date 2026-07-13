import pymupdf  # PyMuPDF library for PDF processing

def read_pdf(file_path):
    # Open the PDF file
    document = pymupdf.open(file_path)
    
    # Initialize an empty string to hold the text
    text = ""
    
    # Iterate through each page in the PDF
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    
    document.close()
    return text

if __name__ == "__main__":
    pdf_file = "Anjali_Gupta_Resume.pdf"  # Replace with your PDF file path
    extracted_text = read_pdf(pdf_file)
    print(extracted_text)