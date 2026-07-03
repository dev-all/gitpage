import sys
import os

def main():
    try:
        from pypdf import PdfReader
    except ImportError:
        print("pypdf is not installed in this environment.")
        # Let's try importing PyPDF2 or other libraries if pypdf fails
        try:
            from PyPDF2 import PdfReader
        except ImportError:
            print("PyPDF2 is also not installed.")
            sys.exit(1)

    pdf_path = r"g:\GNA-DOC\GNA-2026\rescalafonamiento\Respuesta\If reescalafonamiento020726.pdf"
    txt_path = r"g:\GNA-DOC\GNA-2026\rescalafonamiento\Respuesta\If_reescalafonamiento020726.txt"

    print(f"Reading PDF: {pdf_path}")
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
        print(f"Successfully extracted text to: {txt_path}")
    except Exception as e:
        print(f"Error during PDF extraction: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
