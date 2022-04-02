import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all(): 
    if bucket.name.startswith("prod"):
        print (bucket.name)
