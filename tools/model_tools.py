import os
import joblib

from sklearn.model_selection import (
    train_test_split
)

from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    mean_squared_error,
    r2_score
)

from core.model_registry import (
    CLASSIFICATION_MODELS,
    REGRESSION_MODELS
)

from tools.preprocessing_tools import (
    create_preprocessor
)


def train_models(
    df,
    target,
    problem_type
):

    X = df.drop(
        columns=[target]
    )

    y = df[target]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
            if problem_type == "classification"
            else None
        )
    )

    preprocessor = create_preprocessor(
        X
    )

    if problem_type == "classification":
        models = CLASSIFICATION_MODELS
    else:
        models = REGRESSION_MODELS

    os.makedirs(
        "models/trained_models",
        exist_ok=True
    )

    results = []

    trained_models = {}

    for name, model in models.items():

        try:

            pipeline = Pipeline(
                steps=[
                    (
                        "preprocessor",
                        preprocessor
                    ),
                    (
                        "model",
                        model
                    )
                ]
            )

            pipeline.fit(
                X_train,
                y_train
            )

            predictions = pipeline.predict(
                X_test
            )

            if problem_type == "classification":

                accuracy = accuracy_score(
                    y_test,
                    predictions
                )

                f1 = f1_score(
                    y_test,
                    predictions,
                    average="weighted"
                )

                result = {
                    "model": name,
                    "accuracy": round(
                        accuracy, 4
                    ),
                    "f1": round(
                        f1, 4
                    )
                }

            else:

                mse = mean_squared_error(
                    y_test,
                    predictions
                )

                r2 = r2_score(
                    y_test,
                    predictions
                )

                result = {
                    "model": name,
                    "mse": round(
                        mse, 4
                    ),
                    "r2": round(
                        r2, 4
                    )
                }

            results.append(result)

            trained_models[name] = pipeline

            filename = (
                name.replace(" ", "_")
                + ".pkl"
            )

            joblib.dump(
                pipeline,
                os.path.join(
                    "models/trained_models",
                    filename
                )
            )

        except Exception as e:

            results.append({
                "model": name,
                "error": str(e)
            })

    valid = [
        x for x in results
        if "error" not in x
    ]

    if not valid:

        raise RuntimeError(
            "No model trained successfully."
        )

    if problem_type == "classification":

        best = max(
            valid,
            key=lambda x: x["f1"]
        )

    else:

        best = max(
            valid,
            key=lambda x: x["r2"]
        )

    return (
        results,
        best["model"],
        trained_models[
            best["model"]
        ]
    )