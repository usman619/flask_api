from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "usman": {
        "age": "24",
        "gender":"M"
        },
    "ahmad": {
        "age": "24",
        "gender":"M"
        }
}

class BasicApi(Resource):
    def get(self,name):
        return names[name]
    def post(self):
        return {"data":"This is a POST response"}

# "/basic-api/<string:name> here string the type and name the variable
api.add_resource(BasicApi,"/basic-api/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)