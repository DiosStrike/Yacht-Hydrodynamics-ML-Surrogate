from src.preprocess import prepare_data
from src.train import run_grid_search, save_best_model

def run_pipeline():
    """
    Main Orchestrator: Executes the end-to-end Machine Learning Pipeline.
    """
    print("Starting Yacht Hydrodynamics ML Pipeline...")
    
    # Step 1: Execute Data Preprocessing Pipeline
    data_path = 'data/m10_bonus.csv'
    X_train, X_test, X_train_scaled, X_test_scaled, y_train, y_test = prepare_data(data_path)
    print("Data preprocessing completed.")

    # Step 2: Run Automated Hyper-parameter Optimization
    print("Running Hyper-parameter Search (GridSearchCV)...")
    models = run_grid_search(X_train, y_train, X_train_scaled)

    # Step 3: Model Evaluation and Final Serialization
    test_mse = save_best_model(models, X_test, X_test_scaled, y_test)
    print(f"Pipeline finished. Final Test MSE: {test_mse:.4f}")
    print("Best model saved in /models folder.")

if __name__ == "__main__":
    run_pipeline()