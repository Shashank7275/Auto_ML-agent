from agno.agent import Agent
from agno.models.google import Gemini

from dotenv import load_dotenv

load_dotenv()

preprocessing_agent = Agent(
    name="Data preprocessing Agent",

    model=Gemini(
        id="gemini-2.5-flash",
        generation_config={"automatic_function_calling": {"disable": True}},
    ),

    instructions=[
        "You are an ML preprocessing expert.",
        "Explain numerical preprocessing.",
        "Explain categorical preprocessing.",
        "Explain imputation.",
        "Explain encoding.",
        "Explain scaling.",
        "Explain data leakage prevention."
    ],


    markdown=True

)