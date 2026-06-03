import os
from pypdf import PdfReader

def main():
    root_dir = r"g:\GNA-DOC\GNA-2026\rescalafonamiento\Normativa GNA\misEstudios"
    output_file = r"g:\GNA-DOC\GNA-2026\rescalafonamiento\certs_dump.txt"

    with open(output_file, "w", encoding="utf-8") as out:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for file in filenames:
                if file.lower().endswith('.pdf'):
                    filepath = os.path.join(dirpath, file)
                    out.write(f"\n{'='*80}\n")
                    out.write(f"FILE: {os.path.relpath(filepath, root_dir)}\n")
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
