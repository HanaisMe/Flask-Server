import os, json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class MockAPI(Resource):

    @staticmethod
    def get(path=''):
        return '[GET] path: \'%s\'' % path
    
    @staticmethod
    def post(path=''):
        filePath = path.split("?")[0]

        if filePath == 'hello':
            return app.send_static_file('hello.html')
            
        responseFileName = os.path.abspath('response/' + filePath + '.json')
        if os.path.isfile(responseFileName):
            return json.load(open(responseFileName)), 201
        return "Mocked response file NOT found",404

api.add_resource(MockAPI, '/', '/<path:path>') # Catch-All URL

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True)
