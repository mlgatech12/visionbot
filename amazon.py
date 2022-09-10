import logging
import boto3
import os
from botocore.exceptions import ClientError

def upload_file(file_name, bucket):  
    print("a")
    try:
        object_name = "images/" + os.path.basename(file_name)
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        print(e)
        return False


    return True

if __name__ == "__main__":
    s3_client = boto3.client('s3')
    #response = s3_client.list_buckets()
    # Output the bucket names
    print('Existing buckets:')
    print("File uploaded = ", upload_file("app.py", "visionbot2022"))
    