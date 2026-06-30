# Claude Task Agent

> An autonomous AI agent built on the Claude API — give it a high-level goal, it plans, executes, and delivers.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Status](https://img.shields.io/badge/status-active-brightgreen)]()

---

## What It Does

```
User: "Research the top 5 AWS certifications and build me a 30-day study plan"

Agent:
  Step 1 → web_search("top AWS certifications 2026")
  Step 2 → web_search("AWS SAA-C03 study plan 30 days")
  Step 3 → write_file("aws_study_plan.md", <structured plan>)
  Step 4 → Done. Plan saved to /outputs/
```

The agent loops autonomously — observing tool results, updating its plan, and continuing — until the goal is complete or the step limit is reached.

---

## Why It's Interesting

Building an agentic loop on top of an LLM introduces real engineering problems this project solves for:

- **Runaway loops** — step limits and stop conditions prevent infinite tool calls
- **Context degradation** — session memory logs each step's output so the model stays grounded
- **Tool reliability** — the registry pattern isolates failures; one bad tool doesn't crash the agent
- **Extensibility** — adding a tool is two steps, no changes to core loop logic

---

## Architecture

```
main.py
  └── agent/
      └── agent.py          # Core loop: prompt → tool call → observe → repeat
      └── prompts.py        # System prompt and goal injection
  └── tools/
      └── registry.py       # Maps tool names to functions + schemas
      └── web_search.py     # Web search via Brave Search API
      └── write_file.py     # Write markdown/text files to /outputs/
      └── read_file.py      # Read files back into agent context
      └── calculator.py     # Safe math evaluation
  └── memory/
      └── session.py        # Step-by-step log: what ran, what returned
  └── outputs/              # All agent-generated files land here (gitignored)
  └── examples/             # Curated sample outputs — see what the agent produces
  └── .env                  # API keys (never committed)
  └── requirements.txt
```

See [`examples/`](examples/) for real, unedited outputs the agent generated from a single goal each.

---

## Setup

### 1. Clone and install

```bash
git clone https://github.com/Paul-Gifford/claude-task-agent
cd claude-task-agent
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
```

Edit `.env` with your keys:

```env
ANTHROPIC_API_KEY=your_key_here
BRAVE_API_KEY=your_key_here
```

Get your keys:
- Anthropic API: https://console.anthropic.com/
- Brave Search API: https://api.search.brave.com/ *(free tier: 2,000 searches/month)*

### 3. Run

```bash
python main.py
```

Enter a goal when prompted. The agent prints each step and saves output files to `/outputs/`.

---

## Example Goals

```
"Research the top 5 Python web frameworks and compare them in a markdown table"
"What are the AWS SAA exam topics? Create a 4-week study schedule"
"Find 3 recent AI agent news stories and summarize each in 2 sentences"
"Calculate compound interest on $10,000 at 7% for 20 years and explain the result"
```

---

## Tool Reference

| Tool | Description | Input |
|------|-------------|-------|
| `web_search` | Live web search via Brave API | `query` (string) |
| `write_file` | Write content to `/outputs/` | `filename`, `content` |
| `read_file` | Read a file back into agent context | `filename` |
| `calculator` | Evaluate a math expression safely | `expression` (string) |

---

## Adding a Tool

Two steps:

1. Create `tools/my_tool.py` — define a function and a JSON schema
2. Register it in `tools/registry.py`

The agent picks it up on next run. No changes to core loop logic required.

---

## What This Demonstrates

| Concept | Implementation |
|--------|----------------|
| Claude API tool use / function calling | Core agentic pattern throughout |
| Agent loop architecture | Goal → decompose → execute → observe → iterate |
| Session memory | Step log maintains context across tool calls |
| Extensible tool registry | Drop-in tools via function + schema pattern |
| Error isolation | Registry pattern contains tool failures |
| Clean Python project structure | venv, .env, requirements.txt, .gitignore |

---

## Roadmap

- [ ] Persistent memory across sessions (SQLite)
- [ ] Streamlit UI frontend
- [ ] Multi-agent: reviewer checks primary agent's output
- [ ] **AWS deployment — Lambda + API Gateway** *(planned as part of AWS SAA portfolio)*
- [ ] **S3 output storage instead of local filesystem** *(planned as part of AWS SAA portfolio)*

---

## License

MIT — see [LICENSE](LICENSE).
