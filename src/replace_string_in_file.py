import sys
import re
from pathlib import Path

def replace_in_file(file_path, old_string, new_string):
    path = Path(file_path)

    text = path.read_text(encoding="utf-8")
    pattern = re.escape(old_string)
    replaced_text = re.sub(pattern, new_string, text)

    path.write_text(replaced_text, encoding="utf-8")
    print(f"Replaced all occurrences of '{old_string}' with '{new_string}' in {file_path}.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python replace_string_in_file.py <file_path> <old_string> <new_string>")
        sys.exit(1)

    file_path = sys.argv[1]
    old_string = sys.argv[2]
    new_string = sys.argv[3]

    if not Path(file_path).is_file():
        print(f"Error: file '{file_path}' not found.")
        sys.exit(1)

    replace_in_file(file_path, old_string, new_string)
