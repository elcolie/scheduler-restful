from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class OneTime(Resource):
    """
    OneTimeHandler
    """
    def post(self):
        data = request.get_json()
        return {'hello': 'world3333'}

api.add_resource(OneTime, '/one_time')

if __name__ == '__main__':
    app.run(debug=True)