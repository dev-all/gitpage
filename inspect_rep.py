import sys
import os

def main():
    try:
        from pypdf import PdfReader
    except ImportError:
        print("pypdf is not installed.")
        sys.exit(1)

    pdf_path = r"g:\GNA-DOC\GNA-2026\rescalafonamiento\Normativa GNA\REP-30-01.pdf"
    output_path = r"g:\GNA-DOC\GNA-2026\rescalafonamiento\Normativa GNA\REP-30-01_inspected.txt"
    print(f"Reading: {pdf_path}")
    try:
        reader = PdfReader(pdf_path)
        print(f"Total pages: {len(reader.pages)}")
        
        text_content = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                text_content.append(f"=== PAGE {i+1} ===")
                text_content.append(text)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(text_content))
        print(f"Saved complete text to: {output_path}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
