from tools.web_search import web_search, SCHEMA as WEB_SEARCH_SCHEMA
from tools.write_file import write_file, SCHEMA as WRITE_FILE_SCHEMA
from tools.read_file import read_file, SCHEMA as READ_FILE_SCHEMA
from tools.calculator import calculator, SCHEMA as CALCULATOR_SCHEMA

# All schemas sent to Claude so it knows what tools are available
ALL_SCHEMAS = [
    WEB_SEARCH_SCHEMA,
    WRITE_FILE_SCHEMA,
    READ_FILE_SCHEMA,
    CALCULATOR_SCHEMA,
]

# Maps tool name strings to the actual Python functions
TOOL_MAP = {
    "web_search": web_search,
    "write_file": write_file,
    "read_file": read_file,
    "calculator": calculator,
}


def execute_tool(tool_name: str, tool_input: dict) -> str:
    """
    Look up and execute a tool by name.
    Returns the result as a string for Claude to observe.
    """
    if tool_name not in TOOL_MAP:
        return f"ERROR: Unknown tool '{tool_name}'. Available tools: {', '.join(TOOL_MAP.keys())}"

    func = TOOL_MAP[tool_name]
    try:
        return func(**tool_input)
    except TypeError as e:
        return f"ERROR: Bad arguments for tool '{tool_name}': {str(e)}"
    except Exception as e:
        return f"ERROR: Tool '{tool_name}' raised an exception: {str(e)}"