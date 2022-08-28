================
AWS CostExplorer double groupby to CSV
================

This script use 2 groupby in GetCostAndUsage API and generate a CSV file with first groupby as row name and second groupby as column name.

Example result if you use `SERVICE` as groupby1 and `LIKNEDACCOUNT` as groupby2, and the value is unblended cost.

============== ============ ============ ============ ============
AccountID      AccountID1   AccountID2   AccountID3   AccountID4 
============== ============ ============ ============ ============ 
AWS CloudTrail          0.0
AWS Config             10.0
...
AWS Lambda             13.3
AWS Glue               11.2
============== ============ ============ ============ ============ 

================
Usage
================
usage: main.py [-h] [-G1 {groupby1}] [-G2 {groupby2}] [-D {day range}]
