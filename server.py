#!/usr/bin/env python
#coding:utf-8
# Author:  D.Z
# Purpose: Backend API
# Created: 01/07/2017

from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from gtfs import Schedule
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Table, Column, Integer, String
import traceback


app = Flask(__name__, static_url_path="")
api = Api(app)


class HelloAPI(Resource):
    #decorators = [auth.login_required]

    def __init__(self):
        #self.reqparse = reqparse.RequestParser()
        #self.reqparse.add_argument('route', type=str, location='json')
        #self.args = self.reqparse.parse_args()
        super(HelloAPI, self).__init__()

    def get(self):
        return {'code': 0, 'message': 'OK', 'data': [],}, 200

class AgencyListAPI(Resource):
    #decorators = [auth.login_required]

    def __init__(self):
        #self.reqparse = reqparse.RequestParser()
        #self.reqparse.add_argument('route', type=str, location='json')
        #self.args = self.reqparse.parse_args()
        super(AgencyListAPI, self).__init__()
        

    def get(self):
        return {'code': 0, 'message': 'OK', 'data': ['ttc'],}, 200


class StopsAPI(Resource):
    #decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('route', type=str)
        self.args = self.reqparse.parse_args()
        self.sched_ttc = Schedule('./OpenData_TTC_Schedules.db')
        self.sched_ttc_meta = MetaData(bind=self.sched_ttc.engine)
        self.ROUTE_NOT_FOUND = {'code': 20404, 'message': 'Cannot find the route within the system',
                                'data': [],}, 200
        super(StopsAPI, self).__init__()

    def __get_route_id_from_route_number(self, route_number):
        routes_table = Table('routes', self.sched_ttc_meta, autoload=True)
        return int(routes_table.select(routes_table.c.route_short_name == route_number).execute().first()[0])

    @staticmethod
    def __make_query_string_find_stop_name_id_by_route_id(route_id):
        """mother f**king starboy!"""
        return """SELECT stop_name, unique_stops.stop_id
            FROM
                stops,
                (SELECT stop_id, route_id
                 FROM
                 stop_times,
                 (SELECT trip_id, route_id
                  FROM trips
                  WHERE route_id IN ({route_id})
                  GROUP BY shape_id
                  ) AS unique_trips
                 WHERE stop_times.trip_id = unique_trips.trip_id
                 GROUP BY stop_id) AS unique_stops
            WHERE stops.stop_id = unique_stops.stop_id""".format(route_id = route_id)

    def get(self):
        # TODO: could be better
        try:
            route_number = int(self.args['route'])
        except Exception as e:
            return {'code': 20500, 'message': 'Invalid route number',
                    'data': [],}, 200

        # error handling done here, not all numbers are valid routes
        try:
            route_id = self.__get_route_id_from_route_number(route_number)
        except TypeError as e:  # this means nothing found
            return self.ROUTE_NOT_FOUND

        stop_query_string = self.__make_query_string_find_stop_name_id_by_route_id(route_id)

        result = self.sched_ttc.engine.execute(stop_query_string).fetchall()

        # nothing found
        if len(result) == 0:
            return self.ROUTE_NOT_FOUND
        else:
            return {'code': 0, 'message': 'OK', 'data': [[str(i[0]), str(i[1])] for i in result],}, 200


class StopLocationAPI(Resource):
    #decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('stop_code', type=str)
        self.args = self.reqparse.parse_args()
        self.sched_ttc = Schedule('./OpenData_TTC_Schedules.db')
        self.sched_ttc_meta = MetaData(bind=self.sched_ttc.engine)
        self.STOP_NOT_FOUND = {'code': 20404, 'message': 'Cannot find the stop within the system',
                                'data': [],}, 200
        super(StopLocationAPI, self).__init__()

    def get(self):
        try:
            stop_code = int(self.args['stop_code'])
        except Exception as e:
            return {'code': 20500, 'message': 'Invalid stop code',
                    'data': [],}, 200

        stops_table = Table('stops', self.sched_ttc_meta, autoload=True)

        try:
            result = list(stops_table.select(stops_table.c.stop_code == stop_code).execute().first()[4:6])
        except TypeError as e:
            print(e.message)
            print(traceback.print_exc())
            
            return self.STOP_NOT_FOUND

        return {'code': 0, 'message': 'OK', 'data': result}, 200


api.add_resource(AgencyListAPI, '/agency_list', endpoint='')
api.add_resource(StopsAPI, '/stops', endpoint='')
api.add_resource(StopLocationAPI, '/stop_location', endpoint='')
api.add_resource(HelloAPI, '/', endpoint='')

if __name__ == '__main__':
    app.run(debug=True)
