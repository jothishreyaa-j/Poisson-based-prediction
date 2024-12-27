import pandas as pd
from datetime import datetime
from scipy.stats import poisson
import numpy as np

# Function to load the dataset
def load_dataset(file_path):
    # Load the dataset into a DataFrame
    df = pd.read_csv(file_path)
    return df

# Function to aggregate calls by hour
def aggregate_calls_by_hour(df):
    # Convert the 'Call Time' column to datetime format
    df['Call Time'] = pd.to_datetime(df['Call Time'], errors='coerce')  # Handle parsing errors

    # Extract the hour from the 'Call Time' column
    df['Hour'] = df['Call Time'].dt.hour

    # Group by the hour and count the number of calls per hour
    hourly_calls = df.groupby('Hour').size().reset_index(name='Number of Calls')

    return hourly_calls


# Function to simulate calls using Poisson distribution (this is for prediction, not affecting total calls)
def simulate_poisson_calls(hourly_calls, calls_per_day, num_hours=24):
    # Calculate the average number of calls per hour (lambda)
    lambda_per_hour = calls_per_day / num_hours  # Set lambda based on the total expected calls per day
    predictions = []

    # Simulate the number of calls for each hour using the Poisson distribution
    for hour in range(num_hours):
        # Simulate the number of calls for this hour using the Poisson distribution
        predicted_calls = poisson.rvs(mu=lambda_per_hour)
        predictions.append({'Hour': hour, 'Predicted Calls': predicted_calls})

    prediction_df = pd.DataFrame(predictions)
    return prediction_df

# Main function to run the simulation and predict
def run_simulation(file_path, calls_per_day=20):
    # Step 1: Load the dataset
    df_calls = load_dataset(file_path)

    # Step 2: Aggregate calls by hour
    hourly_calls = aggregate_calls_by_hour(df_calls)

    # Step 4: Simulate calls for each hour using Poisson distribution (for prediction)
    prediction_df = simulate_poisson_calls(hourly_calls, calls_per_day)

    # Step 5: Return the predictions and the hourly calls data
    return prediction_df, hourly_calls

# Example usage
file_path = r"C:\Users\jothishreyaa_j\Downloads\phone_calls_dataset.csv"  # Replace with your dataset path

# Run the simulation
prediction_df, hourly_calls = run_simulation(file_path, calls_per_day=20)

# Print the predictions for each hour in the required format
for index, row in prediction_df.iterrows():
    hour_label = f"{row['Hour']}:00 to {row['Hour']+1}:00"
    print(f"{hour_label}: {row['Predicted Calls']} calls")
