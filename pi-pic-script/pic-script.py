import boto3
import os
from time import sleep, strftime
from picamera import PiCamera
import astral
import datetime
import pytz

pst=pytz.timezone('US/Pacific')
a = astral.Astral()

camera = PiCamera()
camera.resolution = (1024, 768)

s3 = boto3.resource('s3')
bucket = s3.Bucket('image-upload-4793')

city_name = 'SunriverOR'

# create astral location object for sunriver Oregon
l = astral.Location((city_name, 'USA', 43.8694, -121.4334, 'US/Pacific', 4164)) # name, region, lat, long, timezone, elevation

while 1:
    dateToday = datetime.date.today() # get todays date

    sunInfo = l.sun(dateToday, local=True) # Get Sun information for Location

    print('Dawn:    %s' % str(sunInfo['dawn']))
    print('Dusk:    %s' % str(sunInfo['dusk']))

    pictures = 0
    now = pst.localize(datetime.datetime.now()) # get the time of now

    while now < sunInfo['dusk']: # While it is earlier than dusk repeat
        if now < sunInfo['dawn']:
            print('sun has not risen %s' % str(now))
        else:
            print('sun is up take a photo %s picture: %s' % (str(now), str(pictures)))
            timeStamp = strftime("%Y-%m-%d_%X")     # YYYY-mm-dd_time
            fileName = '8_towhee_' + timeStamp + '.jpg'
            camera.annotate_text = fileName
            camera.capture(fileName)
            bucket.upload_file(fileName, fileName)
            os.remove(fileName)
            pictures = pictures + 1
        sleep(900)
        now = pst.localize(datetime.datetime.now()) # get the time of now

    print('Finished Taking pictures for the day sun has gone. Total pictues: %s' % str(pictures))

    tomorrowCheck = datetime.date.today() # get todays date
    while dateToday == tomorrowCheck:
        sleep(900)
        tomorrowCheck = datetime.date.today()
