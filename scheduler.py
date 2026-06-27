import pandas as pd
import os

# 1. Read the Excel file safely
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'inputs.xlsx')

try:
    df = pd.read_excel(file_path)
    df = df.dropna(subset=['Name', 'Role']) # Clean empty rows
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
    exit()

# 2. Get the total weekly store hours budget from the manager
try:
    total_store_hours = float(input("Enter the total available hours for the store this week: "))
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

print(f"\nTotal Weekly Budget: {total_store_hours} hours")
print("--------------------------------------------------")

# ==========================================
# STEP 2 - FIXED VS VARIABLE STAFF SEPARATION
# ==========================================

# Define which roles belong to the fixed hour category
fixed_roles = ['Store Manager', 'mini job']

# Filter the DataFrame into two separate groups using Pandas .isin()
df_fixed = df[df['Role'].isin(fixed_roles)].copy()
df_variable = df[~df['Role'].isin(fixed_roles)].copy() # The ~ means "NOT in"

# Calculate total hours locked in by the fixed staff
total_fixed_hours = df_fixed['Contract_Hours'].sum()

# Calculate the remaining budget left over for everyone else
remaining_budget = total_store_hours - total_fixed_hours

print(f"Hours locked by Fixed Staff (Manager + Minijobs): {total_fixed_hours} hrs")
print(f"Remaining budget left for Variable Staff: {remaining_budget} hrs")
print(f"Number of variable employees to split this budget: {len(df_variable)}")

# Check if we even have enough hours to cover the fixed staff
if remaining_budget < 0:
    print("⚠️ CRITICAL WARNING: Total store hours budget is too low to even cover the Fixed Staff!")