import json
import boto3
import io
from io import StringIO
import pandas as pd

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        s3_Bucket_Name = event.get("bucket")
        s3_File_Name = event.get("path")
        
        object = s3_client.get_object(Bucket=s3_Bucket_Name, Key=s3_File_Name)
        body = object['Body']
        csv_string = body.read().decode('utf-8')
        dataframe = pd.read_csv(StringIO(csv_string))
        
        print(dataframe.head(3))

    except Exception as err:
        print(err)
        
    return {
        'statusCode': 200
    }



