import json
import numpy as np
import pandas as pd
import xgboost as xgb

def run_xgboost(json_input):
    # Parse the JSON input
    data_dict = json.loads(json_input)
    
    # Convert the dictionary to a DataFrame
    data_df = pd.DataFrame(data_dict)
    
    # Prepare data for XGBoost
    dmatrix = xgb.DMatrix(data_df)
    
    # Load or define your XGBoost model
    # For demonstration, we'll create a simple model
    params = {
        'objective': 'reg:squarederror',
        'max_depth': 3,
        'learning_rate': 0.1,
        'n_estimators': 100
    }
    model = xgb.train(params, dmatrix, num_boost_round=10)
    
    # Make predictions
    predictions = model.predict(dmatrix)
    
    # Convert predictions to JSON format
    output_json = json.dumps(predictions.tolist())
    
    return output_json

# Example usage
#json_input = '{"feature1": [1, 2, 3], "feature2": [4, 5, 6]}'
#output_json = run_xgboost(json_input)
print("Input JSON:", json_input)
print("Output JSON:", output_json)
