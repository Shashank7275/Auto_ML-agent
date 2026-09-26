def clean_dataset(df):

    df = df.copy()

    rows_before = len(df)

    duplicates = int(df.duplicated().sum())

    missing_values_before = int(df.isna().sum().sum())

    #Remove duplicates
    df = df.drop_duplicates()

    #Numerical Columns

    numerical_cols = df.select_dtypes(include="number").columns

    for col in numerical_cols:
        if df[col].isna().any():

            median = df[col].median()
            df[col] = df[col].fillna(median)

    # Categorical Columns
    categorical_cols = df.select_dtypes(exclude="number").columns

    for col in categorical_cols:
        if df[col].isna().any():

            mode = df[col].mode()[0]
            df[col] = df[col].fillna(mode)

    missing_values_after = int(df.isna().sum().sum())   

    report = {

        "rows_before": rows_before,
        "rows_after": len(df),
        "duplicates_removed":duplicates,
        "missing_values_before": missing_values_before,
        "missing_values_after": missing_values_after,
    }

    return df, report
