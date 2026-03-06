from pdf2image import convert_from_path
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\Library\bin"

def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)

    full_text = ""

    for i, page in enumerate(pages):
        print(f"Processing page {i+1}...")

        temp_img = f"page_{i}.png"
        page.save(temp_img, "PNG")

        text = pytesseract.image_to_string(temp_img)
        full_text += text + "\n"

        os.remove(temp_img)

    return full_text


if __name__ == "__main__":
    pdf_path = "../data/ocr_sample.pdf"

    text = extract_text_from_pdf(pdf_path)

    print("\n📄 Extracted PDF Text:\n")
    print(text)
