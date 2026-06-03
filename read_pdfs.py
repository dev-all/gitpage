import os
import sys

def main():
    try:
        from pypdf import PdfReader
    except ImportError:
        print("pypdf not installed.")
        sys.exit(1)

    folder = r"c:\Users\leoan\OneDrive\Escritorio\GNA\rescalafonamiento\03. EX-2025-88935562-   -APN-DIRTICOM%GNA CON PASE"
    output_file = "dump3.txt"

    files = [f for f in os.listdir(folder) if f.lower().endswith('.pdf')]
    files.sort()

    with open(output_file, "w", encoding="utf-8") as out:
        for file in files:
            filepath = os.path.join(folder, file)
            out.write(f"\n{'='*80}\n")
            out.write(f"FILE: {file}\n")
            out.write(f"{'='*80}\n\n")
            
            try:
                reader = PdfReader(filepath)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        out.write(text + "\n")
            except Exception as e:
                out.write(f"Error reading {file}: {e}\n")

if __name__ == "__main__":
    main()
