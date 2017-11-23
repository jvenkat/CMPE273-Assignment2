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
    def RecordRoute(self, request_iterator, context):
        point_count = 0
        feature_count = 0
        distance = 0.0
        prev_point = None

        start_time = time.time()
        for point in request_iterator:
            point_count += 1
            if get_feature(self.db, point):
                feature_count += 1
            if prev_point:
                distance += get_distance(prev_point, point)
                prev_point = point
            elapsed_time = time.time() - start_time
        return route_guide_pb2.RouteSummary(point_count=point_count,
                                            feature_count=feature_count,
                                            distance=int(distance),
                                            elapsed_time=int(elapsed_time))
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DatastoreClient(host=args.host)

    val = 'foo'
    print("## PUT Request: value = " + val)
    k=uuid.uuid4().hex
    resp = client.put(k,val)
    print("## PUT Response: key = " + k)




if __name__ == "__main__":
    main()
