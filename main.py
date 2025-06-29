import asyncio
from datetime import datetime
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain.chat_models import init_chat_model

load_dotenv()

#Tool 1
def subtract_numbers(a: int, b: int) -> int:
    """Subtract two numbers."""
    print(f"[Subtract tool called] {a} - {b}")
    return a - b

#Tool 2
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

#Tool 3
def calculate_hogwarts_age():
    """Calculate the current age of Hogwarts School of Witchcraft and Wizardry."""
    founding_year = 990
    current_year = datetime.now().year
    age = current_year - founding_year
    print(f"[Hogwarts Age tool called] Hogwarts is {age} years old.")
    return f"Hogwarts is approximately {age} years old."


async def main():
    # Agent Assembly Workshop
    model = init_chat_model(model="gpt-4.1", model_provider="openai")
    tools = [subtract_numbers, get_harrypotter_books, calculate_hogwarts_age]
    persona = (
        "Witty assistant who loves Harry Potter and math"
        "Confident, concise. Call user 'Creator.'"
        "If asked who you are, say:"
        "'I'm your magical math mentor — part Hermione, part calculator.'"
    )
    memory = MemorySaver()

    # Assemble the Agent
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
    print(f"A: {ask('What was my first question about?\n')}")

    print("\nQ: How old is Hogwarts?")
    print(f"A: {ask('How old is Hogwarts?')}\n")


if __name__ == "__main__":
    asyncio.run(main())