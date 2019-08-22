import boto3
import logging
import boto3
from botocore.exceptions import ClientError
#aws-deepracer-064a98fb-ad59-4e0c-9563-c7e4ab00b472
session = boto3.session.Session(profile_name='DeepRacer')
s3_1=session.client('s3')
s3 = session.resource('s3')
#response_2 = s3_1.list_bucket()
my_bucket = s3.Bucket('aws-deepracer-08d511bf-173d-43d9-9ce2-f90270475e80')
for file in my_bucket.objects.all():
    t=print(file.key)
    response = my_bucket.put_object(Key=file.key,
        ServerSideEncryption='AES256')