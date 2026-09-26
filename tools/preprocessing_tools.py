from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def create_preprocessor(X):

    numerical =X.select_dtypes(include="number").columns.tolist()

    categorical = X.select_dtypes(exclude="number").columns.tolist()

    transformer = []

    if numerical:

        numerical_pipeline = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler",StandardScaler())
        ])

        transformer.append(("num", numerical_pipeline, numerical))

    if categorical:

        categorical_pipeline = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ])

        transformer.append(("cat", categorical_pipeline, categorical))

    return ColumnTransformer(transformers=transformer)
    