'''
################################## client.py #############################
#
################################## client.py #############################
'''
import grpc
import datastore_pb2
import argparse
import rocksdb

PORT = 3000

class DatastoreClient():

    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)
    def replicator(self):
        return self.stub.replicator(datastore_pb2.Request1())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DatastoreClient(host=args.host)
    db1 = rocksdb.DB("lab2.db", rocksdb.Options(create_if_missing=True))
    resp = client.replicator()
    for i in resp:
        k = i.k
        l = i.val
        print(k,l)
        db1.put(k,l)


if __name__ == "__main__":
    main()
