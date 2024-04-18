# Introduction

Here within are contained the different files (python, SQL and TXT) that relate to the assesment task given by Alchemy.

## Installation

For running the scripts you will need to do a pip install with the following libraries - pandas_redshift, boto3 and pandas. (You may have some of them already installed - do a double check.)

```bash
pip install pandas_redshift
pip install boto3
pip install pandas
```

## Usage

Check the .py files to see the two scripts containing firstly the code to transfer the csv files to S3 and the second one for the transfer from the S3 datalake to Redshift.
The scripts may be ran through multiple tools such as VSCode, AWS Lambda, AWS CLI, EC2 etc. 
In regards to scheduling - the scripts can be made to run each and every day at a certain time of day, based upon client requirements or internal needs.
