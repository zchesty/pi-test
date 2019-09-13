import boto3
from time import sleep, strftime
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)

s3 = boto3.resource('s3')
bucket = s3.Bucket('image-upload-4793')

# Camera warm-up time
sleep(2)

while 1:
    timeStamp = strftime("%Y-%m-%d_%X")     # YYYY-mm-dd_time
    fileName = '8_towhee_' + timeStamp + '.jpg'
    camera.capture(fileName)
    bucket.upload_file(fileName, fileName)
    sleep(60)



