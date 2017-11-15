import json
import boto.s3.connection
import boto3


iam=boto3.client('iam')
response = iam.list_access_keys()
print(response)

# print("test successful")