from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
import joblib

def run_grid_search(X_train, y_train, X_train_scaled):
    """
    Training Module: Performs benchmarking and Hyper-parameter tuning via GridSearchCV.
    """
    results = {}

    # Algorithm 1: K-Nearest Neighbors (Requires scaled data)
    knn = KNeighborsRegressor()
    knn_param_grid = {'n_neighbors': [3, 5, 7]}
    knn_grid = GridSearchCV(knn, knn_param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
    knn_grid.fit(X_train_scaled, y_train)
    results['KNN'] = knn_grid.best_estimator_
    print(f"KNN Best MSE: {-knn_grid.best_score_:.4f}")

    # Algorithm 2: Support Vector Regression (Requires scaled data)
    svr = SVR()
    svr_param_grid = {'kernel': ['linear', 'rbf'], 'C': [0.1, 1, 10]}
    svr_grid = GridSearchCV(svr, svr_param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
    svr_grid.fit(X_train_scaled, y_train)
    results['SVR'] = svr_grid.best_estimator_
    print(f"SVR Best MSE: {-svr_grid.best_score_:.4f}")

    # Algorithm 3: Random Forest (Scale-invariant, uses raw data)
    rf = RandomForestRegressor(random_state=42)
    rf_param_grid = {'n_estimators': [100, 200], 'max_depth': [5, 10]}
    rf_grid = GridSearchCV(rf, rf_param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
    rf_grid.fit(X_train, y_train)
    results['RF'] = rf_grid.best_estimator_
    print(f"RF Best MSE: {-rf_grid.best_score_:.4f}")

    return results

def save_best_model(models_dict, X_test, X_test_scaled, y_test):
    """
    Evaluation and Model Serialization.
    """
    # Select best model (Random Forest selected based on baseline performance)
    best_model = models_dict['RF']
    y_pred = best_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    # Serialize the trained model for production use
    joblib.dump(best_model, 'models/best_yacht_model.pkl')
    return mse