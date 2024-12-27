import pandas as pd
import random
from faker import Faker
import numpy as np
from datetime import datetime, timedelta

# Initialize Faker instance to generate fake phone numbers
fake = Faker()

# Set random seed for reproducibility
random.seed(42)

# Generate dataset with 10,000 phone calls
num_calls = 10000
phone_numbers = [fake.phone_number() for _ in range(num_calls)]

# Generate random call times scattered throughout the day
start_time = datetime(2024, 12, 26, 0, 0, 0)  # starting from midnight on December 26th
call_times = []
for _ in range(num_calls):
    random_minutes = random.randint(0, 24 * 60 - 1)  # Random minutes in a day (0 to 1439)
    call_time = start_time + timedelta(minutes=random_minutes)
    call_times.append(call_time)

# Generate random duration for each call (in seconds)
call_durations = [random.randint(30, 600) for _ in range(num_calls)]  # between 30 seconds to 10 minutes

# Generate random call types (inbound or outbound)
call_types = ['Inbound' if random.random() < 0.7 else 'Outbound' for _ in range(num_calls)]

# Generate random call status (answered, missed, etc.)
call_statuses = ['Answered' if random.random() < 0.8 else 'Missed' for _ in range(num_calls)]

# Create a DataFrame
df_calls = pd.DataFrame({
    'Phone Number': phone_numbers,
    'Call Time': call_times,
    'Call Duration (seconds)': call_durations,
    'Call Type': call_types,
    'Call Status': call_statuses
})

# Convert 'Call Duration (seconds)' to minutes
df_calls['Call Duration (minutes)'] = df_calls['Call Duration (seconds)'] / 60

# Drop the original 'Call Duration (seconds)' column
df_calls = df_calls.drop(columns=['Call Duration (seconds)'])

# Update the Call Type column to 'Inbound' for all rows
df_calls['Call Type'] = 'Inbound'

# Save the dataset to a CSV file
df_calls.to_csv('phone_calls_dataset.csv', index=False)

print("Dataset has been saved as 'phone_calls_dataset.csv'")
