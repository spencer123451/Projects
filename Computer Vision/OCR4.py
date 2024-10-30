import pytesseract
import pandas as pd
from PIL import Image
import re

# Set the path to the Tesseract executable (if not already in your PATH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_with_keywords(lines, keywords):
    """
    Extract substrings containing any of the given keywords from OCR lines,
    stopping before encountering a space or '|' symbol after the numbers.
    """
    results = []
    for line in lines:
        for keyword in keywords:
            keyword_lower = keyword.lower()  # Convert keyword to lowercase for case-insensitivity
            line_lower = line.lower()  # Convert line to lowercase for case-insensitivity
            if keyword_lower in line_lower:
                # Find the keyword position
                start_idx = line_lower.find(keyword_lower)
                # Extract text from the keyword position to the end of the line
                text_after_keyword = line[start_idx + len(keyword):].strip()
                # Use regex to find the text up to a space or '|' symbol
                match = re.search(r'^\s*[\d,]+\.\d{2}(?=\s|\|)', text_after_keyword)
                if match:
                    results.append(line[:start_idx + len(keyword)] + match.group().strip())
                else:
                    results.append(line.strip())
                break  # Stop checking further keywords in this line
    return results

def ocr_to_csv(image_path, output_csv_path, keywords):
    # Open the image file
    image = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(image, lang='eng')

    # Split the text into lines
    lines = text.split('\n')

    # Extract substrings containing any of the specified keywords
    extracted_lines = extract_text_with_keywords(lines, keywords)
    for line in extracted_lines:
        print(f'Extracted line: {line}')

    # Create a list of dictionaries to store the lines
    data = [{'Line': line} for line in extracted_lines if line.strip()]

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Export the DataFrame to a CSV file
    df.to_csv(output_csv_path, index=False)

# Example usage
#image_path = 'Example payslip.JPG'
#image_path='Examplepayslip2.JPG'
image_path='Examplepayslip3.PNG'
output_csv_path = 'Example-page.csv'
keywords = ['Basic Pay', 'YTD Gross', 'Period of',"Medical Allowance"]  # Adjust keywords as needed
ocr_to_csv(image_path, output_csv_path, keywords)

print(f'OCR results have been exported to {output_csv_path}')
