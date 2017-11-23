import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import uuid
import rocksdb

from concurrent import futures
li = []
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.db = rocksdb.DB("Assignment2.db", rocksdb.Options(create_if_missing=True))
    def decorator(req):
        def inner(self, request, context):
            key1=request.k.encode('utf-8')
            value1=request.val.encode('utf-8')
            li.append(datastore_pb2.Response1(k=key1,val=value1))
            return req(self,request,context)
        return inner

    def replicator(self,request,context):
        print("**************************")
        while(1):
            for i in li:
                print(i.k)
                yield i
		        li.pop(0)
    @decorator
    def put(self, request, context):

        key = request.k
        value = request.val
        keyy_b=key.encode('utf-8')
        value_b=value.encode('utf-8')
        self.db.put(keyy_b,value_b)

        return datastore_pb2.Response(k=key,val=value)

    def get(self, request, context):
        print("get")
        X = request.data.decode('utf-8')
        value = self.db.get(X)
        print("----------")
        print(value)
        print("**********")
        print(self.db1.get(X))
        return datastore_pb2.Response(k=X,val=value)

def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    datastore_pb2_grpc.add_DatastoreServicer_to_server(MyDatastoreServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
	run('0.0.0.0', 3000)
