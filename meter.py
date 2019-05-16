"""List the parking meters in Jamacia Queens"""



import sys
import urllib.request
import csv   #Comma-Separated Values
import io

#Database is at
#https://data.cityofnewyork.us/Transportation/Parking-Meters-GPS-Coodinates-and-Status/5jsj-cq4s
url = "https://data.cityofnewyork.us/Transportation/Parking-Meters-GPS-Coodinates-and-Status/5jsj-cq4s"

try:
    fileFromUrl = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = fileFromUrl.read() #Read whole file into one big sequenceOfBytes.
fileFromUrl.close()

try:
    s = sequenceOfBytes.decode("utf-8")    #s is a string
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

fileFromString = io.StringIO(s)
lines = csv.reader(fileFromString)      #
#
fileFromString.close()

for line in lines:
    MeterType = [0]
    LONG = float(line[3])
    the_geom = float(line[4])
    MeterNo = float(line[5])
    LAT = float(line[6])
    Status = line [7]                               #type of meter


    print(f"{MeterType} {LONG:12.8f} {the_geom} {MeterNo} ({LAT:11.8f}){Status}")

sys.exit(0)
