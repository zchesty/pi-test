import boto3
import os
from time import sleep, strftime
from picamera import PiCamera
import datetime
import pytz
import astral




city_name = 'SunriverOR'
# create astral location object for sunriver Oregon
l = astral.Location((city_name, 'USA', 43.8694, -121.4334, 'US/Pacific', 4164)) # name, region, lat, long, timezone, elevation



pst=pytz.timezone('US/Pacific')

camera = PiCamera()
camera.resolution = (1024, 768)

bucketName = 'sunriver-display-s3-prod'
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucketName)

while 1:
    dateToday = datetime.date.today() # get todays date
    sunInfo = l.sun(dateToday, local=True) # Get Sun information for Location

    pictures = 1
    now = pst.localize(datetime.datetime.now()) # get the time of now

    while now < sunInfo['dusk']: # While it is earlier than dusk repeat
        if now < sunInfo['dawn']:
            print('Sun has not risen. No picture taken')
        else:
            print('Sun is up take a photo. Count: %s' % (str(pictures)))
            timeStamp = strftime("%Y-%m-%d_%X")     # YYYY-mm-dd_time
            fileName = '8_towhee_' + timeStamp + '.jpg'
            camera.annotate_text = fileName
            camera.capture(fileName)

            keys = []
            for s3_file in bucket.objects.all():
                keys.append({'Key': s3_file.key})
            if len(keys) > 0:
                bucket.delete_objects(Delete={
                    'Objects': keys
                })
            bucket.upload_file(fileName,'public/' + fileName)
            os.remove(fileName)

            pictures = pictures + 1
        sleep(1800)
        now = pst.localize(datetime.datetime.now()) # get the time of now

    print('Finished Taking pictures for the day sun has gone. Total pictues: %s' % str(pictures))

    tomorrowCheck = datetime.date.today() # get todays date
    while dateToday == tomorrowCheck:
        sleep(900)
        tomorrowCheck = datetime.date.today()
