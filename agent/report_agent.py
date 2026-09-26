from agno.agent import Agent
from agno.models.google import Gemini

from dotenv import load_dotenv

load_dotenv()


report_agent = Agent(

    name="AutoML Report Agent",

    model=Gemini(
        id="gemini-2.5-flash",
        generation_config={"automatic_function_calling": {"disable": True}},
    ),

    instructions=[
        "Create a professional AutoML report.",
        "Summarize the dataset.",
        "Summarize cleaning.",
        "Summarize preprocessing.",
        "Summarize EDA.",
        "Compare model results.",
        "Explain the selected model.",
        "Mention limitations.",
        "Never invent results."
    ],

    markdown=True
)