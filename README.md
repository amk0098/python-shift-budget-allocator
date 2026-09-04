# Shift Budget Allocator

A Python tool for planning weekly staff hours against a fixed store-hours budget.

The current prototype reads employee information from an Excel workbook, separates fixed-hour roles from variable-hour roles, and calculates the remaining hours available for allocation.

## Current functionality

- Loads employee data from an Excel file
- Removes incomplete employee records
- Identifies fixed roles such as store managers and mini-job staff
- Calculates hours already committed to fixed staff
- Calculates the remaining weekly hours budget for variable staff
- Warns when the total budget cannot cover fixed staffing commitments

## Input format

The current prototype expects an `inputs.xlsx` file next to `scheduler.py` with at least:

| Column | Purpose |
| --- | --- |
| `Name` | Employee name |
| `Role` | Employee role |
| `Contract_Hours` | Contracted weekly hours |

## Run

```bash
python scheduler.py
```

## Roadmap

- Validate missing or invalid contract-hour values
- Add a configurable role policy instead of hard-coded roles
- Export a suggested allocation as CSV
- Add tests for budget calculations
- Build a small dashboard for scenario comparison

## Technology

Python · pandas · Excel input processing

## Status

Early prototype. The repository documents the first working calculation step; the roadmap above defines the path to a fuller planning tool.

## Author

Arian Mohammadkhani
