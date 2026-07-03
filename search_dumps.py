import re

files = ["dump.txt", "dump2.txt", "dump3.txt"]
search_pattern = re.compile(r"1198|206|896|1669|1810", re.IGNORECASE)

for filename in files:
    filepath = f"g:\\GNA-DOC\\GNA-2026\\rescalafonamiento\\{filename}"
    print(f"\nSearching in {filename}...")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if search_pattern.search(line):
                    # print first 100 characters of matching line
                    print(f"L{i}: {line.strip()[:120]}")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
