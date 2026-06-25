import ast
import math
import operator

SCHEMA = {
    "name": "calculator",
    "description": "Safely evaluate a mathematical expression. Supports basic arithmetic, powers, square roots, and common math functions.",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "A math expression to evaluate. Examples: '1000 * (1 + 0.07) ** 20', 'sqrt(144)', '(15 * 12) / 4'",
            }
        },
        "required": ["expression"],
    },
}

# Whitelist of allowed operations and functions
SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
}

SAFE_FUNCTIONS = {
    "sqrt": math.sqrt,
    "abs": abs,
    "round": round,
    "floor": math.floor,
    "ceil": math.ceil,
    "log": math.log,
    "log10": math.log10,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "pi": math.pi,
    "e": math.e,
}


def _safe_eval(node):
    """Recursively evaluate an AST node using only whitelisted operations."""
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError(f"Unsupported constant type: {type(node.value)}")

    elif isinstance(node, ast.Name):
        if node.id in SAFE_FUNCTIONS:
            return SAFE_FUNCTIONS[node.id]
        raise ValueError(f"Unknown name: {node.id}")

    elif isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in SAFE_OPERATORS:
            raise ValueError(f"Unsupported operator: {op_type}")
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        return SAFE_OPERATORS[op_type](left, right)

    elif isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in SAFE_OPERATORS:
            raise ValueError(f"Unsupported unary operator: {op_type}")
        operand = _safe_eval(node.operand)
        return SAFE_OPERATORS[op_type](operand)

    elif isinstance(node, ast.Call):
        func = _safe_eval(node.func)
        if not callable(func):
            raise ValueError("Not a callable function")
        args = [_safe_eval(arg) for arg in node.args]
        return func(*args)

    else:
        raise ValueError(f"Unsupported expression type: {type(node)}")


def calculator(expression: str) -> str:
    """
    Safely evaluate a math expression without using eval().
    """
    try:
        tree = ast.parse(expression, mode="eval")
        result = _safe_eval(tree.body)

        # Format nicely
        if isinstance(result, float):
            if result == int(result):
                formatted = f"{int(result):,}"
            else:
                formatted = f"{result:,.4f}".rstrip("0").rstrip(".")
        else:
            formatted = f"{result:,}"

        return f"Result: {formatted}\nExpression: {expression}"

    except ZeroDivisionError:
        return "ERROR: Division by zero"
    except (ValueError, TypeError) as e:
        return f"ERROR: Invalid expression — {str(e)}"
    except SyntaxError:
        return f"ERROR: Could not parse expression: {expression}"