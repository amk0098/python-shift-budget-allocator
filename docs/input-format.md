# Input workbook format

The prototype expects an Excel workbook named `inputs.xlsx` in the project root.

## Required columns

| Column | Type | Example | Description |
| --- | --- | --- | --- |
| `Name` | text | `Alex Schmidt` | Employee identifier |
| `Role` | text | `Store Manager` | Job role used by allocation policy |
| `Contract_Hours` | number | `20` | Contracted weekly working hours |

## Example

| Name | Role | Contract_Hours |
| --- | --- | ---: |
| Alex Schmidt | Store Manager | 40 |
| Samira Kaya | Sales Associate | 20 |
| Robin Fischer | mini job | 10 |

## Current role policy

The first prototype treats `Store Manager` and `mini job` as fixed-hour roles. All other roles are treated as variable-hour staff.

This policy is intentionally documented here because it is currently hard-coded in `scheduler.py`. A future version should make it configurable.
