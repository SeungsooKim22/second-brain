from pathlib import Path
from input_handler import load_text

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "examples" / "sample_input.txt"

text = load_text(file_path)

print(text)