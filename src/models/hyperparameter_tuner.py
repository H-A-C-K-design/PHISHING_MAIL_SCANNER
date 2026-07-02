from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression


def tune_logistic_regression(X_train, y_train):
    param_grid = {"C": [0.1, 1, 10], "solver": ["liblinear", "lbfgs"]}
    model = LogisticRegression(max_iter=1000)
    grid = GridSearchCV(model, param_grid, cv=3)
    grid.fit(X_train, y_train)
    return grid.best_estimator_
