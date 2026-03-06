import cv2
import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def preprocess_image(image_path):

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.medianBlur(gray, 3)
    thresh = cv2.threshold(
        denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]
    return thresh


def extract_text(image_path):
    processed_img = preprocess_image(image_path)
    temp_file = "temp_processed.png"
    cv2.imwrite(temp_file, processed_img)
    text = pytesseract.image_to_string(Image.open(temp_file))
    os.remove(temp_file)
    return text


if __name__ == "__main__":
    image_path = "../data/sample2.png"

    print("🔍 Running OCR...")
    extracted_text = extract_text(image_path)

    print("\n📄 Extracted Text:\n")
    print("-----------------------------------")
    print(extracted_text)
    print("-----------------------------------")
