# PyGeoIP Locator example
# Base code from Syngress book by TJ O'Connor with modifications

# Two prerequisites:
# 1. Local copy of MaxMind GeoLiteCity database
# 2. pygeoip library by Jennifer Ennis via pip install pygeoip (github hosts)


import pygeoip
gi = pygeoip.GeoIP('/opt/GeoIP/GeoLiteCity.dat')

def printRecord(tgt):
	rec = gi.record_by_name(tgt)
	city = rec['city']
	region = rec['region_code']
	country = rec['country_name']
	long = rec['longitude']
	lat = rec['latitude']
	print('[*] Target: ' + tgt + ' Geolocated. ')
	print('[+] '+str(city)+', '+str(region)+', '+str(country))

# Enter the IP you wish to locate
tgt = '8.8.8.8'
tgt2 = '4.2.2.2'

printRecord(tgt)
printRecord(tgt2)
print('No additional targets.  Job completed.')

# -30-