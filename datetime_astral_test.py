import astral
import datetime
import pytz

from time import sleep

pst=pytz.timezone('US/Pacific')
a = astral.Astral()

city_name = 'SunriverOR'


# create astral location object for sunriver Oregon
l = astral.Location((city_name, 'USA', 43.8694, -121.4334, 'US/Pacific', 4164)) # name, region, lat, long, timezone, elevation

dateToday = datetime.date.today() # get todays date

sunInfo = l.sun(dateToday, local=True) # Get Sun information for Location

now = pst.localize(datetime.datetime.now()) # get the time of now

print('Dawn:    %s' % str(sunInfo['dawn']))
print('Sunrise: %s' % str(sunInfo['sunrise']))
print('Noon:    %s' % str(sunInfo['noon']))
print('Sunset:  %s' % str(sunInfo['sunset']))
print('Dusk:    %s' % str(sunInfo['dusk']))
print('now: %s' % str(now))

print (now < sunInfo['dusk'])


while now < sunInfo['dusk']: # While it is earlier than dusk repeat
    if now < sunInfo['dawn']:
        print('sun has not risen %s' % str(now))
    else:
        print('sun is up take a photo %s' % str(now))
    sleep(30)
    now = pst.localize(datetime.datetime.now()) # get the time of now




