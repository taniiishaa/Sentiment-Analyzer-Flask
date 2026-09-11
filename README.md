# ⚡ Agentic AI Engineering — 16 Days of Building, Breaking & Learning

> **A hands-on learning repository from my Codenoids 2026 Industrial Training in Agentic AI.**
>
> Not just notes. Not just tutorials.  
> This repository captures the progression from **Python + problem solving → asynchronous systems → modern AI applications → tool-calling agents → middleware → MCP**.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Agentic_AI-1C3C3C?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLMs-black?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Apps-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![MCP](https://img.shields.io/badge/MCP-Tool_Connectivity-6E56CF?style=for-the-badge)

</p>

---

## 🧭 What This Repository Really Is

Agentic AI can look deceptively simple from the outside:

```text
User → AI → Answer
```

But while building applications, I learned that the interesting part is everything **between** the question and the answer.

This repository follows that journey:

```text
                    ┌──────────────────────────┐
                    │   Problem Solving        │
                    │  DSA + Python Foundations │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   Async Programming      │
                    │  Tasks • Coroutines • I/O │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   Application Layer      │
                    │ React • FastAPI • APIs   │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   LLM Applications       │
                    │ Ollama • LangChain       │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   Agentic Workflows      │
                    │ Tools • Routing • Agents │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   AI ↔ Tool Connectivity │
                    │ Middleware • MCP/FastMCP │
                    └──────────────────────────┘
```

The goal was not to memorize frameworks.  
The goal was to understand **how the pieces fit together**.

---

# 🗺️ The 16-Day Learning Map

| Phase | Days | Main Focus |
|---|---:|---|
| 🧱 Foundations | 1–3 | Python + DSA + problem solving |
| ⚙️ Concurrency | 4–6 | `asyncio`, tasks, failure handling, BFS, stacks |
| 🧰 Developer Environment | 7–8 | `venv`, `pip`, `uv`, LangChain, Ollama, linked lists |
| 🎨 Frontend Layer | 9–10 | React, Vite, Tailwind, FastAPI, Uvicorn |
| 🌐 Web Fundamentals | 11 | HTTP, storage, cookies, decorators, Lighthouse |
| 🤖 Agentic AI Begins | 12–13 | Streamlit, Ollama, LangChain, tools, GitHub Assistant |
| 🧠 Agent Control | 14–15 | Middleware, model/tool orchestration, AI application flow |
| 🔌 AI Connectivity | 16 | MCP + FastMCP servers and clients |

---

# 🔥 Day 12 — The Turning Point

One of the biggest jumps in the training was moving from **using an LLM** to building a system where an LLM could **choose and use tools**.

### GitHub Assistant

The project combines:

- Streamlit
- LangChain
- ChatOllama
- Qwen 2.5 (0.5B)
- HTTPX
- AsyncIO
- GitHub REST API
- Tool calling

The idea:

```text
                     User
                       │
                       │ Natural-language question
                       ▼
              ┌─────────────────┐
              │   Streamlit UI  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Local LLM      │
              │  ChatOllama     │
              └────────┬────────┘
                       │
                "Which tool?"
                       │
                       ▼
              ┌─────────────────┐
              │ GitHub Tools    │
              │  Tool Selection │
              └────────┬────────┘
                       │
                 Async HTTPX
                       │
                       ▼
              ┌─────────────────┐
              │   GitHub API    │
              │   Live Data     │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ LLM formats the │
              │ final response  │
              └────────┬────────┘
                       │
                       ▼
                     User
```

This was an important conceptual shift:

> **The model is no longer only generating text — it can participate in a workflow.**

---

# 🧩 How Tool Calling Changes an AI Application

A traditional chatbot:

```text
Question
   ↓
LLM
   ↓
Generated Answer
```

A tool-enabled assistant:

```text
Question
   ↓
LLM
   ↓
Understand Intent
   ↓
Select Tool
   ↓
Execute Tool
   ↓
Receive External Data
   ↓
LLM
   ↓
Final Answer
```

That difference is one of the central ideas explored throughout this repository.

---

# 🧠 Day 13 — Teaching the Model to Use Tools

The next step was going deeper into the mechanics of tool-enabled agents.

Topics included:

- LangChain tools
- `@tool`
- Pydantic schemas
- `BaseModel`
- `Field`
- `args_schema`
- `create_agent()`
- `HumanMessage`
- `invoke()`
- Tool response metadata
- Error handling
- Streamlit integration
- Ollama + Qwen

### Example mental model

```text
                    ┌───────────────┐
                    │    User       │
                    └───────┬───────┘
                            ▼
                    ┌───────────────┐
                    │     Agent     │
                    └───────┬───────┘
                            │
                    ┌───────┴────────┐
                    ▼                ▼
             ┌───────────┐    ┌───────────┐
             │    LLM    │    │   Tools   │
             └─────┬─────┘    └─────┬─────┘
                   │                │
                   └───────┬────────┘
                           ▼
                    Final Response
```

The calculator exercise was intentionally small, but the concept scales to much larger systems.

---

# 🧪 Day 14–15 — What Happens Around the Agent?

Once an agent exists, another question appears:

**How do we observe, control, or modify what happens during execution?**

That led into:

### Middleware

```text
                ┌─────────────────┐
                │      Agent      │
                └────────┬────────┘
                         │
                ┌────────▼────────┐
                │   Middleware    │
                │                 │
                │ before_agent    │
                │ before_model    │
                │ after_model     │
                │ after_agent     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Model / Tool  │
                └─────────────────┘
```

The training explored middleware hooks, execution flow, model selection, and tool-call monitoring.

Day 15 also brought the pieces together conceptually:

```text
                         USER
                           │
                           ▼
                    ┌─────────────┐
                    │  Streamlit  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   FastAPI   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    Agent    │
                    └──────┬──────┘
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
             ┌─────────┐       ┌─────────┐
             │   LLM   │       │  Tools  │
             └─────────┘       └─────────┘
```

---

# 🔌 Day 16 — Enter MCP

The final stage introduced **Model Context Protocol (MCP)** and **FastMCP**.

Instead of every AI application creating its own custom connection to every tool, MCP provides a standardized way to expose tools and interact with them.

### The idea

Without a shared protocol:

```text
AI A ───── Custom API ───── Calculator
AI B ───── Different API ── Calculator
AI C ───── Another API ──── Calculator
```

With MCP:

```text
                    AI Client
                       │
                       ▼
                  ┌──────────┐
                  │   MCP    │
                  │ Protocol │
                  └────┬─────┘
                       │
                 ┌─────┴─────┐
                 ▼           ▼
           ┌──────────┐ ┌──────────┐
           │ Calculator│ │  Other   │
           │   Tools   │ │  Tools   │
           └──────────┘ └──────────┘
```

FastMCP made the concept practical in Python by allowing ordinary Python functions to be exposed as tools.

### Hands-on MCP work

The repository contains:

- FastMCP server
- MCP client
- Calculator MCP server
- Calculator MCP client
- Tool definitions
- Async client calls

Example:

```python
@mcp.tool
def add(x: int, y: int):
    return x + y
```

A normal Python function becomes an MCP-accessible tool.

---

# 🏗️ The Repository as a Learning Architecture

Rather than viewing this as 16 unrelated folders, I see it as a stack:

```text
┌─────────────────────────────────────────────┐
│                 MCP / FastMCP               │
│        Standardized AI ↔ Tool Access        │
├─────────────────────────────────────────────┤
│              Agentic AI Layer               │
│       Agents • Tools • Middleware           │
├─────────────────────────────────────────────┤
│                 LLM Layer                   │
│        LangChain • Ollama • Qwen            │
├─────────────────────────────────────────────┤
│             Application Layer               │
│       Streamlit • FastAPI • React           │
├─────────────────────────────────────────────┤
│              Integration Layer              │
│       HTTPX • GitHub REST API • AsyncIO     │
├─────────────────────────────────────────────┤
│              Python Foundations             │
│          DSA • OOP • Async Concepts         │
└─────────────────────────────────────────────┘
```

This layered view is the biggest takeaway from the training.

---

# 📚 What I Worked Through

## 🧱 Python & Problem Solving

LeetCode and algorithmic practice included:

- Two Sum
- Add Two Numbers
- Longest Substring Without Repeating Characters
- Roman to Integer
- Longest Palindromic Substring
- Container With Most Water
- Longest Common Prefix
- Valid Parentheses
- Rotting Oranges
- Merge Two Sorted Lists
- Letter Combinations of a Phone Number

Alongside:

- stacks
- queues
- BFS
- recursion
- backtracking
- linked lists
- two-pointer techniques

---

## ⚡ Asynchronous Programming

Explored:

- coroutines
- `async` / `await`
- event loops
- `asyncio`
- concurrent task execution
- task orchestration
- failure handling
- fail-fast strategies
- success-threshold validation
- asynchronous API calls

A key concept:

```text
Synchronous

Task A ────────────────► Done
                         │
                         ▼
Task B ────────────────► Done


Asynchronous

Task A ────────►
                 \
Task B ───────────► concurrent work
                 /
Task C ────────►
```

---

# 🌐 Web & Backend Foundations

The training also covered the application layer required to build AI systems around models:

### Frontend

- ReactJS
- Vite
- Tailwind CSS
- component architecture
- routing
- responsive UI

### Backend

- FastAPI
- Uvicorn
- REST concepts
- HTTP status codes

### Browser/Web Concepts

- cookies
- local storage
- session storage
- decorators
- Lighthouse

---

# 🤖 AI Stack Explored

| Technology | Role in the Journey |
|---|---|
| **Ollama** | Local LLM runtime |
| **Qwen 2.5 (0.5B)** | Local model used in agent exercises |
| **LangChain** | LLM, tools and agent orchestration |
| **Streamlit** | Rapid AI application interfaces |
| **FastAPI** | Backend/API layer |
| **HTTPX** | Asynchronous HTTP communication |
| **GitHub REST API** | Real-time external data source |
| **FastMCP** | Python implementation for MCP server/client work |
| **React + Vite** | Frontend application development |
| **Tailwind CSS** | UI styling |

---

# 🗂️ Repository Structure

```text
tanisha-agentic-ai-training-2026/
│
├── Day 1/                 # DSA foundations
├── Day 2/
├── Day 3/
│
├── Day 4/                 # AsyncIO
├── Day 5/                 # Async task orchestration
├── Day 6/                 # BFS + Stack
│
├── Day 7/                 # Python environment + LLM basics
├── Day 8/                 # Linked lists + backtracking
│
├── Day 9/                 # React + Vite + Tailwind
├── Day 10/                # FastAPI + Uvicorn
├── Day 11/                # Web concepts + decorators
│
├── Day 12/                # GitHub Assistant
├── Day 13/                # Agents + Tools
├── Day 14/                # Middleware
├── Day 15/                # Agent application architecture
│
├── Day 16/                # MCP + FastMCP
│
└── README.md
```

---

# 🌟 Featured Build: GitHub Assistant

The GitHub Assistant is the strongest practical project inside this training repository.

### What it demonstrates

```text
Natural Language
      ↓
Local LLM
      ↓
Tool Selection
      ↓
Async GitHub API Call
      ↓
Real-Time Data
      ↓
LLM Response
      ↓
Human-Friendly Output
```

It helped connect several concepts that had previously been learned separately:

**LLMs + APIs + tools + async programming + UI + orchestration.**

---

# 🧠 Concepts I Wanted to Understand — Not Just Use

This repository helped me explore questions such as:

- What makes an AI application different from a basic chatbot?
- How does an LLM decide when a tool is useful?
- How can external APIs become tools for an agent?
- Why does asynchronous programming matter for API-heavy applications?
- What role does middleware play around an agent?
- How can a local LLM participate in an application?
- How should frontend, backend and AI layers communicate?
- Why is standardized tool connectivity useful?
- How does MCP fit into the modern AI application stack?

---

# 🛠️ Running the Examples

This repository contains **independent daily exercises and experiments**, not one single application.

Because different days use different technologies, each folder may have its own setup.

Typical Python setup:

```bash
python -m venv .venv
```

Activate on Windows:

```powershell
.venv\Scripts\activate
```

Install the dependencies required by the specific exercise.

For local LLM exercises, Ollama must also be installed and the relevant model must be available locally.

For example:

```bash
ollama pull qwen2.5:0.5b
```

For Streamlit applications:

```bash
streamlit run app.py
```

For FastAPI applications:

```bash
uvicorn main:app --reload
```

> **Note:** Commands are exercise-specific. Check the relevant day's files before running a project.

---

# 📈 From Learning Syntax to Designing Systems

The most valuable part of this training was the progression.

```text
WRITE CODE
   ↓
SOLVE PROBLEMS
   ↓
UNDERSTAND ASYNC EXECUTION
   ↓
BUILD APIS
   ↓
CONNECT TO LLMs
   ↓
GIVE LLMs TOOLS
   ↓
BUILD AGENT WORKFLOWS
   ↓
CONTROL EXECUTION WITH MIDDLEWARE
   ↓
CONNECT AI TOOLS THROUGH MCP
```

That progression changed the way I think about AI development.

Instead of asking only:

> **"Which model should I use?"**

I started thinking about:

> **"What should the model be able to access, decide, call, and return?"**

---

# 🚀 What Comes Next?

This repository is a foundation rather than the final destination.

The next step is to turn these concepts into larger, production-oriented systems involving:

- persistent state and memory
- stronger tool orchestration
- structured outputs
- authentication and authorization
- databases
- observability
- evaluation
- deployment
- containerization
- cloud infrastructure
- multi-agent workflows
- MCP-based integrations

The goal is to move from **learning agentic AI concepts** to **engineering reliable AI-powered systems**.

---

# 📝 Final Takeaway

This repository represents one of the most important phases of my development journey:

**from writing Python programs → to understanding how modern AI systems are assembled.**

It contains the experiments, notes, exercises, prototypes, and small systems that helped me build that understanding step by step.

> **Build small. Understand deeply. Connect the pieces. Then build bigger.**

---

<p align="center">
  <b>Codenoids 2026 · Agentic AI Industrial Training</b><br>
  Learning by building, debugging, experimenting, and connecting ideas.
</p>
