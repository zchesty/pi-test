import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
bucket = s3.Bucket('image-upload-4793')

# Print out bucket names

print(bucket.name)
bucket.upload_file('requirements.txt', 'test.txt')