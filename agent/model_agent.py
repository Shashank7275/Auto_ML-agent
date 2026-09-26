from agno.agent import Agent
from agno.models.google import Gemini

from dotenv import load_dotenv

load_dotenv()

model_agent = Agent(
    name="Model Agent",

    model=Gemini(
        id="gemini-2.5-flash",
        generation_config={"automatic_function_calling": {"disable": True}},
    ),

    instructions=[
        "You are a machine learning expert.",
        "Analyze supplied model metrics.",
        "Compare models.",
        "Explain the selected model.",
        "Never invent metrics."
    ],

    markdown=True
)