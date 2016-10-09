from flask import Flask
from flask import request,jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)

api = Api(app)

class Home(Resource):
    def get(self):
        return jsonify(status='OK')

class Control(Resource):
    def get(self):
        try: 
            #Llamar clase y metodo del gps
            return jsonify(status='OK',message='updated successfully')
        except Exception as e:
            return jsonify(status='ERROR',message=str(e))

class Measure(Resource):
    def get(self):
        return jsonify(status='OK')
        

class gps(Resource):
    def get(self):
        try:
            ResponseList = []
        except Exception as e:
            return str(e)
        return json.dumps(ResponseList)

class sonar(Resource):
    def get(self):
        return jsonify(status='OK')

class uht(Resource):
    def get(self):
        return jsonify(status='OK')

class ia(Resource):
    def get(self):
        return jsonify(status='OK')
 
class test(Resource):
    def post(self):
        return jsonify(status='OK', message="this is a test")

api.add_resource(Home, '/Home')
api.add_resource(Control, '/Control')
api.add_resource(Measure, '/Measure')
api.add_resource(gps, '/gps')
api.add_resource(sonar, '/sonar')
api.add_resource(uht, '/uht')
api.add_resource(ia, '/ia')
api.add_resource(test, '/test')

if __name__ == '__main__':
    app.run()
