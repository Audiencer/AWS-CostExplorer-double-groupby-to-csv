#!/usr/bin/env python3

import argparse
import boto3
import pandas as pd
import datetime

dimension_choices = ['AZ', 'REGION', 'INSTANCE_TYPE', 'LEGAL_ENTITY_NAME', 'INVOICING_ENTITY', 'LINKED_ACCOUNT', 'OPERATION', 'PLATFORM', 'PURCHASE_TYPE', 'SERVICE', 'TENANCY', 'RECORD_TYPE', 'USAGE_TYPE']

parser = argparse.ArgumentParser()
parser.add_argument('-D', '--day', help='specify day range', default=30)
parser.add_argument('-G1', '--group1', help='specify first groupby', choices=dimension_choices, default='SERVICE')
parser.add_argument('-G2', '--group2', help='specify second groupby', choices=dimension_choices, default='REGION')
args = parser.parse_args()

now = datetime.datetime.utcnow()
start = (now - datetime.timedelta(days=args.day)).strftime('%Y-%m-%d')
end = now.strftime('%Y-%m-%d')

session = boto3.Session()
ce = session.client('ce', 'us-east-1')

df = pd.DataFrame(index=[f'{args.group2}_SUM']).isnull()
data=ce.get_cost_and_usage(TimePeriod={'Start': start, 'End':  end}, Granularity='MONTHLY', Metrics=['UnblendedCost'], GroupBy=[ {'Type': 'DIMENSION', 'Key': args.group1}, {'Type': 'DIMENSION', 'Key': args.group2}]) 

for group in data['ResultsByTime'][0]['Groups']:
    service_cost = round(float(group['Metrics']['UnblendedCost']['Amount']),2)
    group1 = group['Keys'][0]
    group2 = group['Keys'][1]
    df.loc[group1, group2] = service_cost 
for column in df.columns:
    df.loc[f'{args.group2}_SUM',column] = df[column].sum()

df.to_csv(f'CostExplore_groupby_{args.group1.lower()}_{args.group2.lower()}.csv')