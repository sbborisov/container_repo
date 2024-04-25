import pandas as pd
import boto3
import pandas_redshift as pr

#Getting the credentials
session = boto3.Session()
credentials = session.get_credentials()
current_credentials = credentials.get_frozen_credentials()

client = boto3.client(
's3',
aws_access_key_id=current_credentials.access_key,
aws_secret_access_key=current_credentials.secret_key)

secret = boto3.client(
'secretsmanager',
aws_access_key_id=current_credentials.access_key,
aws_secret_access_key=current_credentials.secret_key)

#Getting the redshift table name
response = secret.get_secret_value(SecretId = 'redshift secret name')['SecretString']

#Connection to the Redshift DB
pr.connect_to_redshift(dbname = response['dbname'],
                        host = response['host'],
                        port = response['port'],
                        user = response['user'],
                        password = response['password'])

bucket_name = 's3-simeon-borisov-container'

#Connecting to the bucket
pr.connect_to_s3(aws_access_key_id = current_credentials.access_key,
                aws_secret_access_key = current_credentials.secret_key,
                bucket = bucket_name)

#Writing the Dataframe to redshift
objects = client.list_objects(Bucket=bucket_name)['Contents']
for obj in objects:
    df = pd.read_csv(f's3://{bucket_name}/{obj['Key']}')

    #Creating the table name after taking it from the csv file name
    pr.pandas_to_redshift(data_frame = df,
                        redshift_table_name = obj['Key'].split('/')[-1].split('.')[0])


