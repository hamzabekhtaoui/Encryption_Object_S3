import boto3
import sys
import os
import logging
import boto3
from botocore.exceptions import ClientError
region_name_1=['us-east-2','us-east-1','us-west-1','us-west-2']
for each_region in region_name_1:
    session = boto3.session.Session(profile_name='PowerUserAccess',region_name=each_region)
    ec2_re_ob=session.resource("ec2")
    for each_instance in ec2_re_ob.instances.all():
        print(each_instance)
        print(each_region)
#volumes = ec2_re_ob.volumes.all()
#for vol in volumes:
#    iv = volumes.Volume(str(vol.id))
#    if str(iv.encrypted):
#            print("ebs chiffre")
#    else:
#            print(str(iv.encrypted))