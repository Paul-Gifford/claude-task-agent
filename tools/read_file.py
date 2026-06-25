import os
import re

OUTPUTS_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")

SCHEMA = {
    "name": "read_file",
    "description": "Read the contents of a file previously written to the outputs directory.",
    "input_schema": {
        "type": "object",
        "properties": {
            "filename": {
                "type": "string",
                "description": "The filename to read. Example: study_plan.md",
            }
        },
        "required": ["filename"],
    },
}


def read_file(filename: str) -> str:
    """
    Read a file from the outputs directory.
    """
    safe_filename = re.sub(r"[^\w\-. ]", "_", os.path.basename(filename))
    filepath = os.path.join(OUTPUTS_DIR, safe_filename)

    if not os.path.exists(filepath):
        # List available files to help the agent recover
        try:
            available = os.listdir(OUTPUTS_DIR)
            files_list = ", ".join(available) if available else "none"
        except OSError:
            files_list = "unknown"
        return f"ERROR: File '{safe_filename}' not found. Available files: {files_list}"

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        return f"Contents of {safe_filename}:\n\n{content}"
    except OSError as e:
        return f"ERROR: Could not read file: {str(e)}"