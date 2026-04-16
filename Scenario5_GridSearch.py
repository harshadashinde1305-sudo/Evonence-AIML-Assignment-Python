Scenario 5: Hyperparameter Tuning
Python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def tune_model(X_train, y_train):
    model = RandomForestClassifier()
    
    param_grid = {
        "max_depth": [3, 5, 7],
        "n_estimators": [50, 100]
    }
    
    grid = GridSearchCV(model, param_grid, cv=5)
    grid.fit(X_train, y_train)
    
