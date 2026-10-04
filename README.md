# Shift Budget Allocator

A simple Python tool for planning weekly staff hours against a fixed store-hours budget.

The program reads employee data from Excel, keeps fixed staff hours protected, distributes the remaining budget proportionally among variable staff, and exports the result as CSV.

## How it works

1. Load employee data from `inputs.xlsx`
2. Separate fixed and variable staff
3. Calculate fixed staff hours
4. Calculate the remaining weekly budget
5. Distribute the remaining hours according to each variable employee's contract hours
6. Export the suggested allocation to `allocation.csv`

## Input

The `inputs.xlsx` file should contain:

| Column | Purpose |
|---|---|
| `Name` | Employee name |
| `Role` | Employee role |
| `Contract_Hours` | Contracted weekly hours |

Fixed roles currently include:

- Store Manager
- mini job

All other roles are treated as variable staff.

## Allocation logic

The variable budget is distributed proportionally:

`Allocated Hours = Remaining Budget × Employee Contract Hours / Total Variable Contract Hours`

This means employees with larger contracts receive a larger share of the available variable hours.

## Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python scheduler.py
```

Enter the total weekly store-hours budget when asked.

The program creates:

```text
allocation.csv
```

## Technology

Python · pandas · Excel · CSV

## Status

Working prototype for weekly staff-hour budget allocation.

## Author

Arian Mohammadkhani
