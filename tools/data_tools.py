import pandas as pd

def load_dataset(file_path):

    if file_path.lower().endswith(".csv"):
        return pd.read_csv(file_path)

    if file_path.lower().endswith(".json"):
        return pd.read_json(file_path)

    if file_path.lower().endswith(".xlsx"):
        return pd.read_excel(file_path)

    raise ValueError(
        "Unsupported file format. Please provide a CSV, JSON, or Excel file."
        
    )

def get_profile(df):

    numerical_cols = df.select_dtypes(
        include=['number','float']
    ).columns.tolist()

    categorical_cols = df.select_dtypes(
        include=['object','category']
    ).columns.tolist()

    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "numerical_columns": numerical_cols,
        "categorical_columns": categorical_cols,
        "missing_values": df.isnull().sum().to_dict(),
        "describe": df.describe(include='all').to_dict(),
        "duplicates": int(df.duplicated().sum()),

    }