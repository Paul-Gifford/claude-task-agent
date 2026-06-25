import os
import re

OUTPUTS_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")

SCHEMA = {
    "name": "write_file",
    "description": "Write content to a file in the outputs directory. Use markdown (.md) for structured documents.",
    "input_schema": {
        "type": "object",
        "properties": {
            "filename": {
                "type": "string",
                "description": "Filename including extension. Example: study_plan.md or report.txt",
            },
            "content": {
                "type": "string",
                "description": "The full content to write to the file.",
            },
        },
        "required": ["filename", "content"],
    },
}


def write_file(filename: str, content: str) -> str:
    """
    Write content to the outputs directory.
    Sanitizes filename to prevent path traversal.
    """
    # Sanitize: strip path separators, only allow safe characters
    safe_filename = re.sub(r"[^\w\-. ]", "_", os.path.basename(filename))
    if not safe_filename:
        return "ERROR: Invalid filename"

    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUTS_DIR, safe_filename)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        char_count = len(content)
        return f"SUCCESS: Wrote {char_count} characters to outputs/{safe_filename}"
    except OSError as e:
        return f"ERROR: Could not write file: {str(e)}"