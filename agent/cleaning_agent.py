from agno.agent import Agent
from agno.models.google import Gemini

from dotenv import load_dotenv

load_dotenv()

cleaning_agent = Agent(
    name="Data Cleaning Agent",

    model=Gemini(
        id="gemini-2.5-flash",
        generation_config={"automatic_function_calling": {"disable": True}},
    ),

    instructions=[
        "You are a data cleaning expert.",
        "Interpret the cleaning tool results.",
        "Explain missing value treatment.",
        "Explain duplicate handling.",
        "Never claim an operation happened unless the tool result confirms it."
    ],

    markdown=True
)   
