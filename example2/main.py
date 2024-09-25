from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class BasicApi(Resource):
    def get(self):
        return {"data":"This is a GET response"}
    def post(self):
        return {"data":"This is a POST response"}

api.add_resource(BasicApi,"/basic-api")

if __name__ == "__main__":
    app.run(debug=True)