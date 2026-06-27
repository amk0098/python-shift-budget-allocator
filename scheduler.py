import pandas as pd
import os

# Find the exact folder where this script (scheduler.py) is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Link it directly to your file name (change to 'inputs.xlsx' or 'input.xlsx' depending on your exact filename)
file_path = os.path.join(script_dir, 'inputs.xlsx')

try:
    df = pd.read_excel(file_path)
    print(f"Data loaded successfully from: {file_path}")
except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
    print("Double check that the spelling matches your file name exactly (e.g., input vs inputs).")
    exit()

# 2. Get the dynamic weekly budget from the manager
try:
    total_store_hours = float(input("Enter the total available hours for the store this week: "))
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

# 3. Display the starting data
print(f"\nTotal Weekly Budget: {total_store_hours} hours")
print("\n--- Staff Roster ---")
print(df)