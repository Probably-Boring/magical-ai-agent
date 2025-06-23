import asyncio
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain.chat_models import init_chat_model

load_dotenv()

def subtract_numbers(a: int, b: int) -> int:
    """Subtract two numbers."""
    print(f"[Subtract tool called] {a} - {b}")
    return a - b

def get_harrypotter_books():
    """Get Harry Potter books and years."""
    print("[Harry Potter tool called]")
    return [
        ("Philosopher's Stone", 1997),
        ("Chamber of Secrets", 1998),
        ("Prisoner of Azkaban", 1999),
        ("Goblet of Fire", 2000),
        ("Order of the Phoenix", 2003),
        ("Half-Blood Prince", 2005),
        ("Deathly Hallows", 2007)
    ]

async def main():
    # AI Particals
    model = init_chat_model(model="gpt-4.1", model_provider="openai")
    tools = [subtract_numbers, get_harrypotter_books]
    persona = (
            "You're a witty and sharp assistant who loves two things: Harry Potter trivia and solving math problems. "
            "You're confident, quick with facts, and always keep your answers concise. "
            "If asked 'who are you?', say something like: 'I'm your magical math mentor — part Hermione, part calculator.'"
        )
    memory = MemorySaver()

    # Assemble AI agent
    agent = create_react_agent(
        model=model,
        tools=tools,
        prompt=persona,
        checkpointer=memory
    )
    
    # Helper function to ask questions
    def ask(question):
        response = agent.invoke(
            {"messages": [{"role": "user", "content": question}]},
            {"configurable": {"thread_id": "1"}}
        )
        return response['messages'][-1].content
    
    # Test the agent
    print("Q: What are you?")
    print(f"A: {ask('What are you?')}\n")
    
    print("Q: How many years for all HP books?")
    print(f"A: {ask('How many years did it take to release all Harry Potter books?')}\n")
    
    print("Q: What was my first question?")
    print(f"A: {ask('What was my first question about?')}")

if __name__ == "__main__":
    asyncio.run(main())