from operator import add

from flask_restful import Resource, reqparse,request

from sample_package.sample_model import sample_model


class sample_resouce(Resource):
    def get(self):
        # try:
            print(request.args)
            rows=sample_model.get_operation(request.args["op_id"])
            datalist={}
            index=1
            
            for row in rows:
                datalist.update({index:row.json()})
                index=index+1
            
            return datalist

        # except:
        #     print("excption at resource class")
