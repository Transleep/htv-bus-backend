#!flask/bin/python

"""Alternative version of the ToDo RESTful server implemented using the
Flask-RESTful extension."""

from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal

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
        super(StopsAPI, self).__init__()

    def get(self):
        #print(self.args)
        try:
            route_number = int(self.args['route'])
        except Exception as e:
            return {'code': 20500, 'message': 'Invalid route number',
                    'data': [],}, 200
        
        if route_number == 24:
            return {'code': 0, 'message': 'OK', 'data': [['stop_name_1', 'stop_number_1'],
                                                         ['stop_name_2', 'stop_number_2'],
                                                         ],}, 200
        else:
            return {'code': 20404, 'message': 'Cannot find the route within the system',
                    'data': [],}, 200


class StopLocationAPI(Resource):
    #decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('stop_code', type=str)
        self.args = self.reqparse.parse_args()
        super(StopLocationAPI, self).__init__()

    def get(self):
        #print(self.args)
        try:
            stop_code = int(self.args['stop_code'])
        except Exception as e:
            return {'code': 20500, 'message': 'Invalid stop code',
                    'data': [],}, 200
        
        if stop_code == 8426:
            return {'code': 0, 'message': 'OK', 'data': [43.782416,-79.326262]}, 200
        
        elif  stop_code == 8505:
            return {'code': 0, 'message': 'OK', 'data': [43.708605,-79.295762]}, 200
        else:
            return {'code': 20404, 'message': 'Cannot find the stop within the system',
                    'data': [],}, 200


api.add_resource(AgencyListAPI, '/agency_list', endpoint='')
api.add_resource(StopsAPI, '/stops', endpoint='')
api.add_resource(StopLocationAPI, '/stop_location', endpoint='')
api.add_resource(HelloAPI, '/', endpoint='')

if __name__ == '__main__':
    app.run(debug=True)
