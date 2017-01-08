# Transleep API Documentation

##### Ver 1.0

#### Endpoints


##### /agency_list

Give a list of available agencies

###### Arguments: 

None

###### Return: 

List of agencies

```
$ curl "http://htv-bn.ml/agency_list"
{
    "code": 0, 
    "data": [
        "ttc", 
        "yrt", 
        "drt", 
        "grt"
    ], 
    "message": "OK"
}
```


##### /stops?agency=ttc&route=24

Give a list of routes of one certern route number from one certern agency.

###### Arguments:

agency: required: False Type: string The agency of transit

route: required: True Type: string The route number looking into

###### Return: 

list of stop name and stop number

```
$ curl "http://htv-bn.ml/stops?agency=ttc&route=3"
{"message": "OK", "code": 0, "data": [["KENNEDY ARRIVE", "S_KENA"], ["MCCOWAN ARRIVE", "S_MC1A"], ["MCCOWAN STATION - WESTBOUND PLATFORM", "13722"], ["SCARBOROUGH CENTRE STATION - WESTBOUND PLATFORM", "14119"], ["MIDLAND STATION - WESTBOUND PLATFORM", "13726"], ["ELLESMERE STATION - SOUTHBOUND PLATFORM", "13728"], ["LAWRENCE EAST STATION - SOUTHBOUND PLATFORM", "13729"], ["KENNEDY STATION - PLATFORM", "14946"], ["KENNEDY STATION - NORTHBOUND PLATFORM", "14112"], ["LAWRENCE EAST STATION - NORTHBOUND PLATFORM", "13730"], ["ELLESMERE STATION - NORTHBOUND PLATFORM", "13727"], ["MIDLAND STATION - EASTBOUND PLATFORM", "13725"], ["SCARBOROUGH CENTRE STATION - EASTBOUND PLATFORM", "14118"], ["MCCOWAN STATION - PLATFORM", "13721"]]}

$ curl "http://htv-bn.ml/stops?route=99999"
{
    "code": 20404, 
    "data": [], 
    "message": "Cannot find the route within the system"
}

$ curl "http://htv-bn.ml/stops?route=wtf"
{
    "code": 20500, 
    "data": [], 
    "message": "Invalid route number"
}
```


##### /stop_location?agency=ttc&stop_code=10000

Give the exact location data of the stop.

###### Arguments:

agency: required: False Type: string The agency of transit

stop_number: required: True Type: integer a unique stop number 

###### Return: 

A tuple of latitude

```
$ curl "http://htv-bn.ml/stop_location?agency=ttc&stop_code=8426"
{
    "code": 0, 
    "data": [
        43.782416, 
        -79.326262
    ], 
    "message": "OK"
}

$ curl "http://htv-bn.ml/stop_location?stop_code=99999"
{
    "code": 20404, 
    "data": [], 
    "message": "Cannot find the stop within the system"
}

$ curl "http://htv-bn.ml/stop_location?stop_code=wtf"
{
    "code": 20500, 
    "data": [], 
    "message": "Invalid stop code"
}
``` 

