import re

filepath = r"g:\GNA-DOC\GNA-2026\rescalafonamiento\Normativa GNA\REP-30-01_inspected.txt"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for the section "6.004. Reclamos" or "6.004"
matches = [m.start() for m in re.finditer(r"6\.004", content)]

if matches:
    print(f"Found matches for 6.004:")
    for idx, pos in enumerate(matches):
        start = max(0, pos - 100)
        end = min(len(content), pos + 1500)
        print(f"\n--- Match {idx+1} ---")
        print(content[start:end])
else:
    print("No matches for 6.004")

# Let's search for "reclamo" or "recurso" sections
recurso_matches = [m.start() for m in re.finditer(r"RECURSO|RECLAMO", content)]
print(f"\nTotal RECURSO/RECLAMO matches: {len(recurso_matches)}")
