import sys
import os

def extract_pdf_to_txt(pdf_path, txt_path):
    try:
        from pypdf import PdfReader
    except ImportError:
        print("pypdf is not installed.")
        sys.exit(1)

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
        print(f"Saved to: {txt_path}")
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

def main():
    base_dir = r"g:\GNA-DOC\GNA-2026\rescalafonamiento\Normativa GNA"
    files = [
        "DI-2025-1198-APN-DINALGEN#GNA.pdf",
        "DI-2025-206-APN-DINALGEN#GNA.pdf",
        "DI-2021-1810-APN-DINALGEN#GNA  Reescalafonamiento del Personal de Oficial de Escalafón Reclutamiento Local.pdf"
    ]
    for file in files:
        pdf_path = os.path.join(base_dir, file)
        txt_path = os.path.join(base_dir, file.replace(".pdf", ".txt"))
        extract_pdf_to_txt(pdf_path, txt_path)

if __name__ == "__main__":
    main()
