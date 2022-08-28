================
AWS CostExplorer double groupby to CSV
================

This script uses 2 groupby in GetCostAndUsage API and generate a CSV file with the first groupby as row name and the second groupby as column name.

Below is an example result if you use `SERVICE` as groupby1 and `LIKNEDACCOUNT` as groupby2, and the value is unblended cost.

============== ============ ============ ============ ============
AccountID      AccountID1   AccountID2   AccountID3   AccountID4 
============== ============ ============ ============ ============ 
AWS CloudTrail          0.0
AWS Config             10.0
...
AWS Lambda             13.3
AWS Glue               11.2
============== ============ ============ ============ ============ 

Other available groupby options are AZ, INSTANCE_TYPE, LEGAL_ENTITY_NAME, INVOICING_ENTITY, LINKED_ACCOUNT, OPERATION, PLATFORM, PURCHASE_TYPE, SERVICE, TENANCY, RECORD_TYPE, and USAGE_TYPE.

================
Usage
================
usage: main.py [-h] [-G1 {groupby1}] [-G2 {groupby2}] [-D {day range}]
