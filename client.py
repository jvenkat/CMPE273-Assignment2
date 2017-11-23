'''
################################## client.py #############################
#
################################## client.py #############################
'''
import grpc
import datastore_pb2
import argparse
import uuid
PORT = 3000

class DatastoreClient():

    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

    def put(self, k, val):
        return self.stub.put(datastore_pb2.Request(k=k,val=val))
    def get(self, k):
        return self.stub.get(datastore_pb2.Request(k=k,val=val))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DatastoreClient(host=args.host)

    val = 'foo'
    print("## PUT Request: value = " + val)
    k=uuid.uuid4().hex
    response = client.put(k,val)
    print("## PUT Response: key = " + k)
    print("GET Req Key:"+ response.key)
    x = client.get(resp.key)
    print("get req value"+x.value)




if __name__ == "__main__":
    main()
