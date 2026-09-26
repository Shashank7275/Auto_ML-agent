from sklearn.linear_model import (
    LogisticRegression, 
    LinearRegression
)
from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor,
    GradientBoostingClassifier,
    GradientBoostingRegressor,
    AdaBoostClassifier,
    AdaBoostRegressor,
    ExtraTreesClassifier,
    ExtraTreesRegressor
)

from sklearn.tree import (
    DecisionTreeClassifier,
    DecisionTreeRegressor
)

from sklearn.svm import (
    SVC,
    SVR
)

from sklearn.neighbors import ( 
    KNeighborsClassifier,
    KNeighborsRegressor
)

CLASSIFICATION_MODELS = {
    "Logistic Regression": LogisticRegression(
        max_iter=1000
    ),

    "Random Forest Classifier": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "Gradient Boosting Classifier": GradientBoostingClassifier(
        random_state=42
    ),

    "Extra Tree Classifier": ExtraTreesClassifier(
        n_estimators=100,
        random_state=42
    ),

    "Decision Tree Classifier": DecisionTreeClassifier(
        random_state=42
    ),

    "AdaBoost Classifier": AdaBoostClassifier(
        random_state=42
    ),

    "SVM": SVC(),

    "KNN": KNeighborsClassifier()
}

REGRESSION_MODELS = {
    "Linear Regression": LinearRegression(),

    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        random_state=42
    ),

    "Extra tree": ExtraTreesRegressor(
        n_estimators=100,
        random_state=42
    ),

    "AdaBoost": AdaBoostRegressor(
        random_state=42
    ),

    "SVM": SVR(),

    "KNN": KNeighborsRegressor(
        
    )
}

