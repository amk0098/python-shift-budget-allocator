import pandas as pd
import os

# Find the Excel file next to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "inputs.xlsx")

try:
    df = pd.read_excel(file_path)
    df = df.dropna(subset=["Name", "Role"])
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
    exit()

# Ask for the total weekly store-hours budget
try:
    total_store_hours = float(
        input("Enter the total available hours for the store this week: ")
    )
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

print(f"\nTotal Weekly Budget: {total_store_hours} hours")
print("--------------------------------------------------")

# Fixed staff keep their contracted hours
fixed_roles = ["Store Manager", "mini job"]

df_fixed = df[df["Role"].isin(fixed_roles)].copy()
df_variable = df[~df["Role"].isin(fixed_roles)].copy()

# Check contract hours
df["Contract_Hours"] = pd.to_numeric(df["Contract_Hours"], errors="coerce")
df = df.dropna(subset=["Contract_Hours"])

df_fixed = df[df["Role"].isin(fixed_roles)].copy()
df_variable = df[~df["Role"].isin(fixed_roles)].copy()

# Calculate fixed hours and remaining budget
total_fixed_hours = df_fixed["Contract_Hours"].sum()
remaining_budget = total_store_hours - total_fixed_hours

print(f"Hours locked by Fixed Staff: {total_fixed_hours} hrs")
print(f"Remaining budget for Variable Staff: {remaining_budget} hrs")
print(f"Number of variable employees: {len(df_variable)}")

# Check whether the budget can cover fixed staff
if remaining_budget < 0:
    print("WARNING: The budget is too low to cover the fixed staff.")
    exit()

# Check whether there are variable employees to allocate hours to
if len(df_variable) == 0:
    print("No variable employees found.")
    exit()

# Total contract hours of variable staff
total_variable_contract_hours = df_variable["Contract_Hours"].sum()

if total_variable_contract_hours <= 0:
    print("Error: Variable staff have no valid contract hours.")
    exit()

# Give each variable employee a proportional share
df_variable["Allocated_Hours"] = (
    remaining_budget
    * df_variable["Contract_Hours"]
    / total_variable_contract_hours
)

# Keep fixed employees at their contract hours
df_fixed["Allocated_Hours"] = df_fixed["Contract_Hours"]

# Combine the results
result = pd.concat([df_fixed, df_variable], ignore_index=True)

# Save the suggested allocation
output_path = os.path.join(script_dir, "allocation.csv")
result[["Name", "Role", "Contract_Hours", "Allocated_Hours"]].to_csv(
    output_path, index=False
)

print("\nSuggested allocation:")
print(result[["Name", "Role", "Contract_Hours", "Allocated_Hours"]].to_string(index=False))

print(f"\nAllocation saved to: {output_path}")
