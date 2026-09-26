def get_best_model(
        results,
        problem_type
):
    valid = [
        r for r in results
        if "error" not in r
    ]

    if problem_type == "classification":

        return max(
            valid,
            key=lambda x: x["f1"]
            
        )

    return max(
        valid,
        key=lambda x: x["r2"]
    )