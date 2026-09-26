import os

import matplotlib.pyplot as plt
import seaborn as sns

def create_eda(df):

    os.makedirs(
        "output/charts",
        exist_ok=True
    )

    charts = []

    numeric = df.select_dtypes(include="number")

    if not numeric.columns.empty:

        path = (
            "output/charts"
            "/correlation.png"
        )

        plt.figure(figsize=(10, 8))

        sns.heatmap(
            numeric.corr(),
            annot=True,
            fmt=".2f"
        )

        plt.tight_layout()

        plt.savefig(path)

        plt.close()

        charts.append(path)

    return charts