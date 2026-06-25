# Claude Task Agent

A lightweight autonomous AI agent built on the Claude API. Give it a high-level goal, it breaks it into steps, calls real tools (web search, file writing, calculations), and returns a structured output.

---

## What It Does

```
User: "Research the top 5 AWS certifications and build me a 30-day study plan"

Agent:
  Step 1 → web_search("top AWS certifications 2026")
  Step 2 → web_search("AWS SAA-C03 study plan 30 days")
  Step 3 → write_file("aws_study_plan.md", <structured plan>)
  Step 4 → Done. Here's your plan + file saved to /outputs/
```

The agent loop runs until the goal is complete or it hits the step limit.

---

## Architecture

```
main.py
  └── agent/
      └── agent.py          # Core agent loop (prompt → tool call → observe → repeat)
      └── prompts.py        # System prompt and goal injection
  └── tools/
      └── registry.py       # Tool registry — maps tool names to functions
      └── web_search.py     # Web search via Brave Search API
      └── write_file.py     # Write markdown/text files to /outputs/
      └── read_file.py      # Read files back into context
      └── calculator.py     # Safe math evaluation
  └── memory/
      └── session.py        # In-session step log (what happened, what was returned)
  └── outputs/              # All agent-generated files land here
  └── .env                  # API keys (never committed)
  └── requirements.txt
```

---

## Setup

### 1. Clone and install
```bash
git clone https://github.com/YOUR_USERNAME/claude-task-agent
cd claude-task-agent
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env.example .env
```
Edit `.env` and add:
```
ANTHROPIC_API_KEY=your_key_here
BRAVE_API_KEY=your_key_here      # Free tier: 2,000 searches/month
```

Get your keys:
- Anthropic: https://console.anthropic.com/
- Brave Search API: https://api.search.brave.com/

### 3. Run
```bash
python main.py
```

You'll be prompted to enter a goal. The agent runs, prints each step, and saves any output files to `/outputs/`.

---

## Example Goals to Try

- `"Research the top 5 Python web frameworks and compare them in a markdown table"`
- `"What are the AWS SAA exam topics? Create a 4-week study schedule for me"`
- `"Find 3 recent news stories about AI agents and summarize each in 2 sentences"`
- `"Calculate compound interest on $10,000 at 7% for 20 years and explain the result"`

---

## Tool Reference

| Tool | Description | Input |
|------|-------------|-------|
| `web_search` | Search the web via Brave API | `query` (string) |
| `write_file` | Write content to `/outputs/` | `filename`, `content` |
| `read_file` | Read a file from `/outputs/` | `filename` |
| `calculator` | Evaluate a math expression | `expression` (string) |

---

## Project Structure for Recruiters

This project demonstrates:
- **Claude API tool use / function calling** — the core agentic pattern
- **Agent loop architecture** — goal decomposition, tool execution, observation, iteration
- **Session memory** — step-by-step logging so the agent doesn't lose context
- **Extensible tool registry** — new tools drop in with one function and a schema
- **Clean Python project structure** — venv, .env, requirements, gitignore

---

## Extending It

Want to add a tool? Two steps:

1. Create `tools/my_tool.py` with a function and a JSON schema
2. Register it in `tools/registry.py`

The agent picks it up automatically on next run.

---

## Roadmap

- [ ] Persistent memory across sessions (SQLite)
- [ ] Streamlit UI frontend
- [ ] Multi-agent: reviewer agent checks primary agent's output
- [ ] AWS deployment (Lambda + API Gateway)
- [ ] S3 output storage instead of local filesystem

---

## License

MIT
