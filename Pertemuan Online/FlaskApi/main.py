from flask import Flask, request, Response, jsonify, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        # return jsonify({'hello': 'world', 'nama': 'Evan', 'asal': 'Manado'})

        # Dengan respon
        return make_response(jsonify({'hello': 'world', 'nama': 'Evan', 'asal': 'Manado'}), 201)

    def post(self):
        data = request.get_json()
        # return jsonify({'data': data})

        strEvan = f"{data['nama']} berasal dari {data['asal']}"
        return jsonify({'data': strEvan})


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
