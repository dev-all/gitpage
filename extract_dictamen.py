import sys
import os
from pypdf import PdfReader

def main():
    pdf_path = r"g:\GNA-DOC\GNA-2026\rescalafonamiento\Normativa GNA\IF-2024-119942037-APN-DIREMAN%GNA.pdf"
    txt_path = r"g:\GNA-DOC\GNA-2026\rescalafonamiento\Normativa GNA\IF-2024-119942037-APN-DIREMAN%GNA.txt"
    print(f"Reading: {pdf_path}")
    try:
        reader = PdfReader(pdf_path)
        text_content = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                text_content.append(f"--- PAGE {i+1} ---")
                text_content.append(text)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("\n".join(text_content))
        print(f"Successfully extracted to: {txt_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
