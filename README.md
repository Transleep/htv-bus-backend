# Our Great App API Documentation

##### Ver 0.2

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
        "ttc"
    ], 
    "message": "OK"
}
```

For dummy server, only TTC available.

##### /stops?route=24

Give a list of routes of one certern route number from one certern agency.

###### Arguments:

route: required: True Type: string The route number looking into

###### Return: 

list of stop name and stop number

```
$ curl "http://htv-bn.ml/stops?route=3"
{"message": "OK", "code": 0, "data": [["KENNEDY ARRIVE", "13398"], ["MCCOWAN ARRIVE", "13502"], ["MCCOWAN STATION - WESTBOUND PLATFORM", "14541"], ["SCARBOROUGH CENTRE STATION - WESTBOUND PLATFORM", "14542"], ["MIDLAND STATION - WESTBOUND PLATFORM", "14543"], ["ELLESMERE STATION - SOUTHBOUND PLATFORM", "14544"], ["LAWRENCE EAST STATION - SOUTHBOUND PLATFORM", "14545"], ["KENNEDY STATION - PLATFORM", "14546"], ["KENNEDY STATION - NORTHBOUND PLATFORM", "14547"], ["LAWRENCE EAST STATION - NORTHBOUND PLATFORM", "14548"], ["ELLESMERE STATION - NORTHBOUND PLATFORM", "14549"], ["MIDLAND STATION - EASTBOUND PLATFORM", "14550"], ["SCARBOROUGH CENTRE STATION - EASTBOUND PLATFORM", "14551"], ["MCCOWAN STATION - PLATFORM", "14552"]]}

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

For dummy server, try with route 24.

##### /stop_location?stop_code=10000

Give the exact location data of the stop.

###### Arguments:

stop_number: required: True Type: integer a unique stop number 

###### Return: 

A tuple of latitude

```
$ curl "http://htv-bn.ml/stop_location?stop_code=8426"
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

For dummy server, try with stop number 8426 and 8505.
