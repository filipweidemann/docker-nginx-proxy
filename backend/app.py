from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    def get(self):
        return "Hello world!"

api.add_resource(Index, '/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
