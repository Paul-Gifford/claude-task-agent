import os
import anthropic
from rich.console import Console
from rich.panel import Panel

from agent.prompts import SYSTEM_PROMPT, build_goal_message
from tools.registry import ALL_SCHEMAS, execute_tool
from memory.session import SessionMemory

console = Console()

MAX_STEPS = int(os.getenv("MAX_STEPS", 10))
MODEL = os.getenv("MODEL", "claude-sonnet-4-6")


class Agent:
    """
    Core agent loop.

    Each iteration:
      1. Send conversation history to Claude
      2. Claude either calls a tool OR returns a final response
      3. If tool call → execute it, append result to history, loop
      4. If text response with DONE → stop and return summary
    """

    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def run(self, goal: str) -> str:
        memory = SessionMemory(goal)
        messages = [{"role": "user", "content": build_goal_message(goal)}]

        console.print(Panel(
            f"[bold cyan]Goal:[/bold cyan] {goal}",
            title="[bold]Claude Task Agent[/bold]",
            border_style="cyan",
        ))

        for step in range(1, MAX_STEPS + 1):
            console.print(f"\n[dim]─── Step {step}/{MAX_STEPS} ───[/dim]")

            # Call Claude
            response = self.client.messages.create(
                model=MODEL,
                max_tokens=4096,
                system=SYSTEM_PROMPT,
                tools=ALL_SCHEMAS,
                messages=messages,
            )

            # Append Claude's full response to history
            messages.append({"role": "assistant", "content": response.content})

            # Check if Claude is done (no tool calls)
            if response.stop_reason == "end_turn":
                final_text = self._extract_text(response.content)
                console.print(Panel(
                    final_text,
                    title="[bold green]✓ Agent Complete[/bold green]",
                    border_style="green",
                ))
                if memory.files_written:
                    console.print(
                        f"\n[green]Files saved:[/green] {', '.join(memory.files_written)}"
                    )
                return final_text

            # Process tool calls
            tool_results = []
            for block in response.content:
                if block.type != "tool_use":
                    if hasattr(block, "text") and block.text.strip():
                        console.print(f"[italic]{block.text.strip()}[/italic]")
                    continue

                tool_name = block.name
                tool_input = block.input
                tool_use_id = block.id

                # Show what the agent is doing
                console.print(
                    f"[yellow]→ Tool:[/yellow] [bold]{tool_name}[/bold]  "
                    f"[dim]{self._summarize_input(tool_name, tool_input)}[/dim]"
                )

                # Execute the tool
                result = execute_tool(tool_name, tool_input)

                # Log to memory
                memory.log_step(step, tool_name, tool_input, result)

                # Show result preview
                preview = result[:200] + "..." if len(result) > 200 else result
                console.print(f"[dim]  ↳ {preview}[/dim]")

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tool_use_id,
                    "content": result,
                })

            # Add tool results back into the conversation
            if tool_results:
                messages.append({"role": "user", "content": tool_results})

        # Hit step limit
        console.print(
            f"\n[red]Step limit ({MAX_STEPS}) reached.[/red] "
            "Increase MAX_STEPS in .env if the goal needs more steps."
        )
        return f"Step limit reached. Progress: {memory.summary()}"

    def _extract_text(self, content: list) -> str:
        """Pull text blocks out of a response."""
        texts = [block.text for block in content if hasattr(block, "text")]
        return "\n".join(texts).strip()

    def _summarize_input(self, tool_name: str, tool_input: dict) -> str:
        """Short display string for tool input."""
        if tool_name == "web_search":
            return f"query: \"{tool_input.get('query', '')}\""
        if tool_name == "write_file":
            return f"filename: {tool_input.get('filename', '')}"
        if tool_name == "read_file":
            return f"filename: {tool_input.get('filename', '')}"
        if tool_name == "calculator":
            return f"expr: {tool_input.get('expression', '')}"
        return str(tool_input)