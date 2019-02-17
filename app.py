from flask import Flask
from flask_restful import Api
from sample_package.sample_resource import sample_resouce
from sample_package.db_resource import db,DB_URL

sample_app = Flask(__name__)
api = Api(app=sample_app)
sample_app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
sample_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(sample_resouce,'/')

if __name__=="__main__" :
    db.init_app(sample_app)
    sample_app.run(port=4000)

