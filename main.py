import os

LINE = "I finally reached inbox zero by replying-all 'unsubscribe' to the CEO's company-wide email — and HR replied-all 'same.'"

assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} out of range"

out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
