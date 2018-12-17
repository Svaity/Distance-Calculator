


"""
Date Created
@author: Shrey Vaity
Title : Distance Calculator using web api and JSon

"""

import geocoder
from math import sin, cos, asin, pi, sqrt
import urllib
import re


def add(lnk):
	"""To find address"""
    with urllib.request.urlopen(lnk) as response:
        html = str(response.read())
        html.lower()
        lines = html.split("}")
    for line in lines:
        if re.findall(f"matchedAddress", line):
            m = re.search(f'[\w,][\w,][\w,][\d]', line)
            strt = m.start()
            line = line[strt:]
            end = m.end()
            line = line[:end]
            address = line[:-2]
            if "coordin" in address:
                address = address[:-12]
            return address


def location(lnk):
	"""To get the coordinates"""
    with urllib.request.urlopen(lnk) as response:
        html = str(response.read())
        html.lower()
        lines = html.split("}")
    for line in lines:
        if re.findall(f"coordinates", line):
            m = re.search(f'[x]', line)
            st = m.start()
            lx = line[st:]
            offsetx = lx.find(",")
            x = lx[3:offsetx]

    for line in lines:
        if re.findall(f"coordinates", line):
            m = re.search(f'[,"y"]', line)
            offset1 = line.find('"y"')
            st = m.start()
            ly = line[st:]
            offsety = ly.find(",")
            y1 = ly[offset1:]
            y = y1[4:]
    return x, y


def calc(lon1, lat1, lon2, lat2):
	"""calculations for distance"""
    lon1 = float(lon1)
    lat1 = float(lat1)
    lon2 = float(lon2)
    lat2 = float(lat2)
    lon1 = lon1 * 0.017453293
    lat1 = lat1 * 0.017453293
    lon2 = lon2 * 0.017453293
    lat2 = lat2 * 0.017453293
    lati = lat2 - lat1
    lon = lon2 - lon1
    lat = lat2 - lat1
    a = sin(lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lon / 2) ** 2
    c = 2 * asin(sqrt(a))
    R = 3959
    dst = R * c
    return dst


def main():
    lnk = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=1600+Pennsylvania+Ave+NW%2CWashington%2CDC+20500&benchmark=9&format=json"
    print(lnk)
    address1 = add(lnk)
    print(address1)
    x1, y1 = location(lnk)
    print(x1, y1)
    try:
        a1 = input("Enter house")
        a2 = input("STreet_name")
        a3 = input("State")
        lnk3 = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address="+a1+"%2C"+a2+"%2C"+a3+"&benchmark=9&format=json"
        lnk3 = lnk3.replace(" ","+")
        print(lnk3)
        address2 = a1+a2+a3
        x2, y2 = location(lnk3)
        print(x2, y2)
        distance = calc(x1, y1, x2, y2)
        print("The Distance between",address1, "and", address2, "is", distance)
    except UnboundLocalError:
        print("Sorry Not valid address")

if __name__ == '__main__':
    main()