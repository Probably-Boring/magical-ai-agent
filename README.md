# 🪄 Build a Magical AI Agent

Welcome! This guide will teach you how to set up, run, and extend your own magical AI assistant. No need for a long story—let’s get you using your agent right away!

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.13+
- `uv` (or `pip`)

### 2. Install Dependencies
```bash
uv pip install -r pyproject.toml
# or
pip install -r requirements.txt
```

### 3. (Optional) Set Up Environment
If you use API keys (e.g., OpenAI), create a `.env` file and add your credentials.

### 4. Run the Agent
```bash
python main.py
```
You’ll see example questions and magical answers in your terminal!

---

## 🧙 How to Use
- **Ask questions:** The agent can answer general queries, do math, and knows Harry Potter trivia.
- **Memory:** It remembers your previous questions in a session.
- **Tools:** It can subtract numbers, list Harry Potter books, and calculate Hogwarts’ age.

---

## 🛠️ Extending Your Agent
Want to add your own magic?

1. **Add a new tool:**  
   Define a Python function in `main.py` and add it to the `tools` list.
2. **Change the persona:**  
   Edit the `persona` string to give your agent a new style or theme.
3. **Swap the model:**  
   Use a different LLM by changing the model initialization.

**Example:**
```python
def tell_joke():
    return "Why did the wizard cross the road? To get to the other spell!"

tools = [subtract_numbers, get_harrypotter_books, calculate_hogwarts_age, tell_joke]
```

---

## ❓ FAQ
- **How do I reset memory?**  
  Restart the program to clear conversation history.
- **Can I use a different LLM?**  
  Yes! Swap out the model in `main.py`.

---

## 🎉 That’s It!
You’re ready to chat, experiment, and extend your magical AI agent. Happy building!
