import datetime
from datetime import datetime
from os.path import getsize
from xml.etree.ElementTree import tostring

import psycopg2
from click import DateTime
from flask_restful.fields import Boolean, DateTime, Integer
from psycopg2.extensions import Column
from sqlalchemy.orm import query
from sqlalchemy.sql.schema import Column, FetchedValue
from sqlalchemy.types import Integer

from sample_package.db_resource import db


class sample_model(db.Model):

    __table_args__ = {"schema":"logging"}
    __tablename__ = "t_history" 

    id = db.Column( db.Integer, primary_key=True )
    operation = db.Column( db.String )

    def __init__(self,i_id,i_operation):
        self.id=i_id
        self.operation=i_operation

    
    def json(self):
        return{
            "operation_id":self.id,
            "operation":self.operation
        }

    @classmethod
    def get_operation(self,in_id):
        try:
            data=self.query.filter(self.id>in_id).all()
            return data
        except:
            print("exception at model class")
