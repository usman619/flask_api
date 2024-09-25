import os
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name= {self.name}, views= {self.views}, likes= {self.likes})"

# Check if the db already exists
if not os.path.exists("instance/database.db"):
    # Create the database tables inside an application context
    with app.app_context():
        db.create_all()
        print("Database created successfully...")
else:
    print("Database alreadly exists. Skipping database creation...")

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views on the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)


video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views on the video is required")
video_update_args.add_argument("likes", type=int, help="Likes on the video is required")



resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
}


class Video(Resource):

    @marshal_with(resource_fields)
    def get(self,video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video does not exist...")
        return result
    
    @marshal_with(resource_fields)
    def put(self,video_id):
        args = video_put_args.parse_args()

        result = VideoModel.query.filter_by(id=video_id).first()

        if result:
            abort(409, message="Video_id already taken...")
        
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201 # created successfully
    
    @marshal_with(resource_fields)
    def patch(self,video_id):
        args = video_update_args.parse_args()
        result = result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video does not exist...")
        
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
        
        db.session.commit()

        return result, 200


    def delete(self,video_id):
        return '',204 # deleted successfully

        

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)