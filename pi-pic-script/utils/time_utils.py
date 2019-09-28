import astral



def getDayLight(date):
    city_name = 'SunriverOR'
    # create astral location object for sunriver Oregon
    l = astral.Location((city_name, 'USA', 43.8694, -121.4334, 'US/Pacific', 4164)) # name, region, lat, long, timezone, elevation
    l.sun(date, local=True) # Get Sun information for Location
    return l