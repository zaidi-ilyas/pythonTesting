import boto3
import os
client= boto3.client('ec2', region_name='us-east-1')

resp =client.describe_instances()

print(resp['Reservations'][0]['Instances'][0]['InstanceId'])

file_to_upload = 'BackUps/' + "bucket.txt"
bucket = 'theclouduser'
print("HY")
client2= boto3.client('s3')
client2.upload_file("bucket.txt", bucket, file_to_upload)
