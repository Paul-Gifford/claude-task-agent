"""
Quick sanity checks for each tool.
Run with: python -m pytest tests/ -v
Or just: python tests/test_tools.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Windows consoles default to cp1252, which can't encode the ✓/✗ output below.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from tools.calculator import calculator
from tools.write_file import write_file
from tools.read_file import read_file
from tools.registry import execute_tool, TOOL_MAP, ALL_SCHEMAS


# ── Calculator ────────────────────────────────────────────────────────────────

def test_calculator_basic():
    result = calculator("2 + 2")
    assert "4" in result, f"Expected 4, got: {result}"
    print(f"✓ calculator basic: {result}")

def test_calculator_compound_interest():
    result = calculator("10000 * (1 + 0.07) ** 20")
    assert "38" in result, f"Expected ~38697, got: {result}"
    print(f"✓ calculator compound interest: {result}")

def test_calculator_sqrt():
    result = calculator("sqrt(144)")
    assert "12" in result, f"Expected 12, got: {result}"
    print(f"✓ calculator sqrt: {result}")

def test_calculator_division_by_zero():
    result = calculator("1 / 0")
    assert "ERROR" in result
    print(f"✓ calculator div/zero handled: {result}")

def test_calculator_injection_blocked():
    result = calculator("__import__('os').system('ls')")
    assert "ERROR" in result
    print(f"✓ calculator injection blocked: {result}")


# ── File tools ────────────────────────────────────────────────────────────────

def test_write_and_read_file():
    content = "# Test File\n\nThis is a test."
    write_result = write_file("test_output.md", content)
    assert "SUCCESS" in write_result, f"Write failed: {write_result}"
    print(f"✓ write_file: {write_result}")

    read_result = read_file("test_output.md")
    assert "Test File" in read_result, f"Read failed: {read_result}"
    print(f"✓ read_file: found content")

def test_read_missing_file():
    result = read_file("definitely_does_not_exist.md")
    assert "ERROR" in result
    print(f"✓ read_file missing: {result}")

def test_write_file_path_traversal_blocked():
    result = write_file("../../etc/passwd", "bad content")
    assert "SUCCESS" in result
    print(f"✓ write_file path traversal sanitized: {result}")


# ── Registry ──────────────────────────────────────────────────────────────────

def test_registry_has_all_tools():
    expected = {"web_search", "write_file", "read_file", "calculator"}
    assert set(TOOL_MAP.keys()) == expected
    print(f"✓ registry tools: {list(TOOL_MAP.keys())}")

def test_registry_schemas_valid():
    for schema in ALL_SCHEMAS:
        assert "name" in schema
        assert "description" in schema
        assert "input_schema" in schema
    print(f"✓ all {len(ALL_SCHEMAS)} schemas valid")

def test_registry_unknown_tool():
    result = execute_tool("nonexistent_tool", {})
    assert "ERROR" in result
    print(f"✓ registry unknown tool handled: {result}")


# ── Run all ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        test_calculator_basic,
        test_calculator_compound_interest,
        test_calculator_sqrt,
        test_calculator_division_by_zero,
        test_calculator_injection_blocked,
        test_write_and_read_file,
        test_read_missing_file,
        test_write_file_path_traversal_blocked,
        test_registry_has_all_tools,
        test_registry_schemas_valid,
        test_registry_unknown_tool,
    ]

    print("\nRunning tool tests...\n")
    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1

    print(f"\n{'─' * 40}")
    print(f"Results: {passed} passed, {failed} failed")

    if failed > 0:
        sys.exit(1)