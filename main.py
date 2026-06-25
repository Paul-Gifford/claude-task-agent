#!/usr/bin/env python3
"""
Claude Task Agent
-----------------
Give it a goal. It figures out the steps, calls tools, and gets it done.

Usage:
    python main.py                    # Interactive prompt
    python main.py "Your goal here"   # Pass goal as argument
"""

import sys
import os
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()

console = Console()


def check_env():
    """Validate required environment variables before running."""
    missing = []
    if not os.getenv("ANTHROPIC_API_KEY"):
        missing.append("ANTHROPIC_API_KEY")
    if not os.getenv("BRAVE_API_KEY"):
        missing.append("BRAVE_API_KEY (needed for web_search tool)")

    if missing:
        console.print("\n[red]Missing environment variables:[/red]")
        for var in missing:
            console.print(f"  • {var}")
        console.print("\nCopy [bold].env.example[/bold] to [bold].env[/bold] and fill in your keys.")
        if "ANTHROPIC_API_KEY" in missing:
            sys.exit(1)
        else:
            console.print(
                "[yellow]Warning:[/yellow] BRAVE_API_KEY missing — web_search tool will fail.\n"
            )


def get_goal() -> str:
    """Get the goal from CLI args or interactive prompt."""
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])

    console.print("\n[bold cyan]Claude Task Agent[/bold cyan]")
    console.print("─" * 40)
    console.print("[dim]Example goals:[/dim]")
    console.print("  • Research the top 5 AWS certifications and compare them")
    console.print("  • Find 3 recent AI agent news stories and summarize each")
    console.print("  • Calculate compound interest on $10k at 7% for 20 years\n")

    goal = console.input("[bold]Enter your goal:[/bold] ").strip()
    if not goal:
        console.print("[red]No goal provided. Exiting.[/red]")
        sys.exit(1)
    return goal


def main():
    check_env()

    # Import here so .env is loaded first
    from agent.agent import Agent

    goal = get_goal()

    agent = Agent()
    agent.run(goal)


if __name__ == "__main__":
    main()