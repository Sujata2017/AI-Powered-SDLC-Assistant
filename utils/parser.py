import os
import re

def sanitize_filename(filename, index):
    """
    Remove invalid characters and provide fallback filename if needed.
    """
    # Remove characters invalid in Windows/macOS/Linux filenames
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename).strip()

    if not filename or filename.lower().startswith("!doctype"):
        filename = f"file{index}.html"

    return filename



def parse_and_save_code_files(raw_code, base_dir="generated_code"):
    os.makedirs(base_dir, exist_ok=True)
    code_blocks = re.findall(r"```(?:\w+)?\n(.*?)```", raw_code, re.DOTALL)

    if not code_blocks:
        raise ValueError("No valid code blocks found in the generated content.")

    saved_files = []

    for i, block in enumerate(code_blocks):
        # Try to infer file type from first line or use index fallback
        first_line = block.strip().splitlines()[0]
        ext = "py"  # default

        if "html" in first_line.lower():
            ext = "html"
        elif "css" in first_line.lower():
            ext = "css"
        elif "javascript" in first_line.lower() or "js" in first_line.lower():
            ext = "js"

        filename = f"file_{i + 1}.{ext}"
        file_path = os.path.join(base_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(block.strip())

        saved_files.append(file_path)

    return saved_files
