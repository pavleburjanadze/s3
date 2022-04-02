import boto3

client = boto3.client("s3")

response = client.list_buckets()

print("My S3 Buckets are:")

for bucket in response['Buckets']:
    print(f"{bucket['Name']}")
