
#AWS CostExplorer double groupby to CSV


This script use 2 groupby in GetCostAndUsage API and generate a CSV file with first groupby as row name and second groupby as column name.

Example result if you use `SERVICE` as groupby1 and `LIKNEDACCOUNT` as groupby2, and the value is unblended cost.
============== ============ ============ ============ ============ ============ ============
               000000000000 111111111111 222222222222 333333333333 444444444444 555555555555
============== ============ ============ ============ ============ ============ ============
AWS CloudTrail          0.0
AWS Config             10.0
...
AWS Lambda             13.3
AWS Glue               11.2
============== ============ ============ ============ ============ ============ ============

<<<<<<< HEAD:README.md
## Usage
usage: main.py [-h] [-G1 {groupby1}] [-G2 {groupby2}] [-D {day range}]
=======
##Usage
usage: main.py [-h] [-G1 {groupby1}] [-G2 {groupby2}] [-D {day range}]


>>>>>>> b7eefaa95dd55df6b9804f967e1acc967aa12584:ReadMe.txt
