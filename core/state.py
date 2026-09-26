from dataclasses import dataclass, field
from typing import Any


@dataclass
class AutoMLState:

    # Dataset
    file_path: str = ""
    df: Any = None

    # Problem
    target: str | None = None
    problem_type: str | None = None

    # Analysis
    profile: dict = field(default_factory=dict)

    # Cleaning
    cleaning_report: dict = field(default_factory=dict)

    # EDA
    eda_report: dict = field(default_factory=dict)
    charts: list = field(default_factory=list)

    # Models
    model_results: list = field(default_factory=list)
    best_model_name: str | None = None
    best_model: Any = None

    # Report
    report: str = ""