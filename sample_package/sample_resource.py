from operator import add

from flask_restful import Resource, reqparse

from sample_package.sample_model import sample_model

parser = reqparse.RequestParser()
parser.add_argument("database", type = str, help = "Please provide a valid database name")
parser.add_argument("schema", type = str, help = "Please provide a valid schema name")
parser.add_argument("table", type = str, help = "Please provide a valid table name")


class sample_resouce(Resource):
    def get(self):
        try:
            data=parser.parse_args()
            print(data["database"]+data["schema"]+data["table"])
            columns=sample_model.getColumn(data["database"],data["schema"],data["table"])
            column_list={}
            index=1
            
            for column in columns:
                column_list.update({index:column.json()})
                index=index+1
            
            return column_list

        except:
            print("excption at resource class")
