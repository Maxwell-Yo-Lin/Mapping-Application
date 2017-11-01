# Maxwell Lin 46268364
from decimal import Decimal
import urllib.request
import urllib.error
import json
import urllib.parse


x=["4533 Campus Dr, Irvine, CA","1111 Figueroa St, Los Angeles, CA","3799 S Las Vegas Blvd, Las Vegas, NV"]

def parameter_get(locations:list)->dict:
    'returns you a dictionary of a key, and from->(start point) to to->(locations)'
    API_KEY = "JvRZ7MugipA2uJazZnNOTPI68mEmdbKS"
    parameters = [('key', API_KEY)]
    for i in range(len(locations)):
        if i == 0 :
            point = ('from', locations[i])
            parameters.append(point)
        else:
            point = ('to', locations[i])
            parameters.append(point)
#    print (parameters)
    return parameters

def print_steps(data:dict)->str:
    'return the steps from start to destination'
    result = "DIRECTIONS\n"
    for sections in range(len(data["route"]["legs"])):
        for directions in (data["route"]["legs"][sections]["maneuvers"]):
            result += directions["narrative"]+"\n"
    return result

def get_total_distance(data:dict)->str:
    'Returns the distance of the total route in miles'
    distance = round(data["route"]["distance"])
    return "TOTAL DISTANCE: "+str(distance)+" miles"

def get_total_time(data:dict)->str:
    'Returns the time of the total route in minutes'
    time = round((data["route"]["time"])/60)
    return "TOTAL TIME: " + str(time) +" minutes"

def print_latlong(data:dict)->str:
    'returns the latitude and longitude of each location'
    result="LATLONGS\n"
    for i in range(len(data["route"]["locations"])):
        lat=data["route"]["locations"][i]["displayLatLng"]["lat"]
        long=data["route"]["locations"][i]["displayLatLng"]["lng"]

        if lat<0:
            lat = round(Decimal(lat),2)
            lat = str(abs(lat))+"S"
        else:
            lat = round(Decimal(lat),2)
            lat = str(lat)+"N"

        if long<0:
            long = round(Decimal(long),2)
            long = str(abs(long))+"W"
        else:
            long = round(Decimal(long),2)
            long = str(long)+"E"

        result += lat+" "+long+"\n"
    return result


def get_url(parameters):
    'get url for all basic information like distance time etc'
    base_url = "http://open.mapquestapi.com/directions/v2/route?"
#    print (base_url + urllib.parse.urlencode(parameters))
    return (base_url + urllib.parse.urlencode(parameters))

def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    except:
        return {'error':'lol'}

    finally:
        if response != None:
            response.close()



def get_latlong(data:dict)->list:
    'returns a list of pairs of latitude and longitude for each location'
    result = []
    for i in range(len(data["route"]["locations"])):
        lat=data["route"]["locations"][i]["displayLatLng"]["lat"]
        long=data["route"]["locations"][i]["displayLatLng"]["lng"]
        pair = str(lat)+','+str(long)
        result.append(pair)
#    print(result)
    return result


def get_elevation_parameters(latlong:list)->list:
    'returns the list of elevation parameters based on list of latlong pairs'
    API_KEY = "JvRZ7MugipA2uJazZnNOTPI68mEmdbKS"

    parameters=[]

    for i in latlong:
        base = [('key', API_KEY)]
        base.append(('latLngCollection',i))
        parameters.append(base)
#    print (parameters)
    return parameters

def get_elevation_urls(parameters:list)->list:
    'gets the elevation url for our code, which gives us information on elevation, return a list of urls'
    base_url = "http://open.mapquestapi.com/elevation/v1/profile?"
    urls=[]
    for i in parameters:
        url = (base_url + urllib.parse.urlencode(i))
        urls.append(url)
#    print(urls)
    return urls


def get_elevation(data:dict)->str:
    'returns a elevation based on the result from ONE url in feet'
    elevation = round((data["elevationProfile"][0]["height"])*3.280839895)
#    print(elevation)
    return str(elevation)

def get_elevations(url_list:list)->list:
    'returns a list of elevations(str) based on a list of urls'
    elevations=[]
    for url in url_list:
        data = get_result(url)
        elevations.append(get_elevation(data))
#    print (elevations)
    return elevations


"""
url = get_url(parameter_get(x))
result = get_result(url)
print (result)
print(get_total_distance(result))
print(get_total_time(result))
print_steps(result)
print_latlong(result)
get_latlong(result)
print (get_elevation_parameters(get_latlong(result)))
url2 = get_elevation_urls(get_elevation_parameters(get_latlong(result)))
result2= get_result('http://open.mapquestapi.com/elevation/v1/profile?key=JvRZ7MugipA2uJazZnNOTPI68mEmdbKS&latLngCollection=33.648639%2C-117.831268')
get_elevation(result2)
"""
