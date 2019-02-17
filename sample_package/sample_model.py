from sqlalchemy.orm import query
from sample_package.db_resource import db
import datetime
from datetime import datetime
from os.path import getsize
from xml.etree.ElementTree import tostring
import psycopg2
from click import DateTime
from flask_restful.fields import Boolean, DateTime, Integer
from psycopg2.extensions import Column
from sqlalchemy.sql.schema import Column, FetchedValue
from sqlalchemy.types import Integer

class sample_model(db.Model):

    __table_args__ = {"schema":"information_schema"}
    __tablename__ = "columns" 

    table_catalog = db.Column( db.String )
    table_schema = db.Column( db.String )
    table_name = db.Column( db.String )
    column_name = db.Column( db.String, primary_key=True )

    def __init__(self,i_dbname,i_schemaname,i_tablename,i_columnname):
        self.table_catalog=i_dbname
        self.table_schema=i_schemaname
        self.table_name=i_tablename
        self.column_name=i_columnname
    
    def json(self):
        return{
            "database":self.table_catalog,
            "schema_name":self.table_schema,
            "table_name":self.table_name,
            "column_name":self.column_name
        }

    @classmethod
    def getColumn(self,in_database,in_schema,in_table):
        try:
            column=self.query.filter_by(table_catalog=in_database,table_schema=in_schema,table_name=in_table).all()
            print(column)
            return column
        except:
            print("exception at model class")