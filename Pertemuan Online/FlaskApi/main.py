from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return jsonify({'hello': 'world', 'nama': 'Evan', 'asal': 'Manado'})

    def post(self):
        data = request.get_json()
        # return jsonify({'data': data})

        strEvan = f"{data['nama']} berasal dari {data['asal']}"
        return jsonify({'data': strEvan})


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
