from agno.agent import Agent
from agno.models.google import Gemini

from dotenv import load_dotenv

load_dotenv()

evaluation_agent = Agent(

    name="Evaluation Agent",
    model=Gemini(
        id="gemini-2.5-flash",
        generation_config={"automatic_function_calling": {"disable": True}},
    ),

    instructions=[
        "You are an ML evaluation expert.",
        "Interpret accuracy, F1, RMSE and R2.",
        "Identify possible overfitting.",
        "Explain model limitations.",
        "Use only supplied metrics."
    ],
    markdown=True
)
