import pandas as pd
import boto3

#Getting the aws credentials from a local file
with open(r'C:\Users\Simeon.Borisov\Desktop\keys.txt', 'r') as f:
    response = f.readlines()[0].split(',')
    access_key = response[0]
    secret_key = response[1]
    print(access_key, secret_key)

#Prepping the transfer to S3
client = boto3.client(
's3',
aws_access_key_id=access_key,
aws_secret_access_key=secret_key)

csv_list = ['costs', 'FX_Table', 'Country_Table', 'Customer_Table', 'SalesData']

#Looping through all the files to get them inside the datalake (S3)
for x in csv_list:
    url = f'https://raw.githubusercontent.com/sbborisov/container_repo/main/{x}.csv'
    df = pd.read_csv(url)

    df.to_csv(f's3://s3-simeon-borisov-bucket/{x}.csv')


