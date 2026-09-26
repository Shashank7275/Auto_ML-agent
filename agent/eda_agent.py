from agno.agent import Agent
from agno.models.google import Gemini

from dotenv import load_dotenv

load_dotenv()

EDA_agent = Agent(
    name="EDA Agent",

    model=Gemini(
        id="gemini-2.5-flash",
        generation_config={"automatic_function_calling": {"disable": True}},
    ),

    instructions=[
        "You are an exploratory data analysis expert.",
        "Interpret supplied EDA results.",
        "Identify important patterns.",
        "Identify possible correlations.",
        "Never invent chart observations."
    ],

    markdown=True
)