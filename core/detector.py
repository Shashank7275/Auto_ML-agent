import pandas as pd

def suggest_target_column(df):

    columns = list(df.columns)

    if not columns:
        return None

    normalized = {
        str(column).strip().lower().replace(" ", "_"): column
        for column in columns
    }

    for name in (
        "target",
        "target_variable",
        "label",
        "outcome",
        "response",
        "dependent_variable",
        "y"
    ):
        if name in normalized:
            return normalized[name]

    for column in columns:
        name = str(column).strip().lower().replace(" ", "_")
        if name.endswith(("_target", "_label", "_outcome", "_response")):
            return column

    return columns[-1]


def detect_problem_type(df, target):

    y = df[target]

    if not pd.api.types.is_numeric_dtype(y):
        return 'classification'

    unique_values = y.nunique()

    if unique_values <= 10:
        return "classification"

    return "regression"