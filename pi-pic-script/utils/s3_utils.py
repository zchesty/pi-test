
def clearBucket(bucket):
    keys = []
    for s3_file in bucket.objects.all():
        keys.append({'Key': s3_file.key})
    bucket.delete_objects(Delete={
        'Objects': keys
    })
