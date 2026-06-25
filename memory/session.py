from dataclasses import dataclass, field
from typing import Any
from datetime import datetime


@dataclass
class Step:
    step_number: int
    tool_name: str
    tool_input: dict
    tool_result: Any
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class SessionMemory:
    """
    Tracks everything that happened in this agent run.
    Passed back to Claude as tool_result blocks so it never
    loses context across steps.
    """

    def __init__(self, goal: str):
        self.goal = goal
        self.steps: list[Step] = []
        self.files_written: list[str] = []
        self.started_at = datetime.now().isoformat()

    def log_step(self, step_number: int, tool_name: str, tool_input: dict, tool_result: Any):
        step = Step(
            step_number=step_number,
            tool_name=tool_name,
            tool_input=tool_input,
            tool_result=tool_result,
        )
        self.steps.append(step)

        if tool_name == "write_file":
            filename = tool_input.get("filename", "unknown")
            if filename not in self.files_written:
                self.files_written.append(filename)

    def summary(self) -> str:
        lines = [f"Goal: {self.goal}", f"Steps taken: {len(self.steps)}"]
        if self.files_written:
            lines.append(f"Files written: {', '.join(self.files_written)}")
        return " | ".join(lines)