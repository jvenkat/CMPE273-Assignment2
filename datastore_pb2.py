# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datastore.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='datastore.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x64\x61tastore.proto\"!\n\x07Request\x12\t\n\x01k\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\t\"\n\n\x08Request1\"\"\n\x08Response\x12\t\n\x01k\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\t\"#\n\tResponse1\x12\t\n\x01k\x18\x01 \x01(\x0c\x12\x0b\n\x03val\x18\x02 \x01(\x0c\x32p\n\tDatastore\x12\x1c\n\x03put\x12\x08.Request\x1a\t.Response\"\x00\x12\x1c\n\x03get\x12\x08.Request\x1a\t.Response\"\x00\x12\'\n\nreplicator\x12\t.Request1\x1a\n.Response1\"\x00\x30\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='k', full_name='Request.k', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='val', full_name='Request.val', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=52,
)


_REQUEST1 = _descriptor.Descriptor(
  name='Request1',
  full_name='Request1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=64,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='k', full_name='Response.k', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='val', full_name='Response.val', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=100,
)


_RESPONSE1 = _descriptor.Descriptor(
  name='Response1',
  full_name='Response1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='k', full_name='Response1.k', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='val', full_name='Response1.val', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=137,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Request1'] = _REQUEST1
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Response1'] = _RESPONSE1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Request1 = _reflection.GeneratedProtocolMessageType('Request1', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST1,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Request1)
  ))
_sym_db.RegisterMessage(Request1)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

Response1 = _reflection.GeneratedProtocolMessageType('Response1', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE1,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Response1)
  ))
_sym_db.RegisterMessage(Response1)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class DatastoreStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.put = channel.unary_unary(
          '/Datastore/put',
          request_serializer=Request.SerializeToString,
          response_deserializer=Response.FromString,
          )
      self.get = channel.unary_unary(
          '/Datastore/get',
          request_serializer=Request.SerializeToString,
          response_deserializer=Response.FromString,
          )
      self.replicator = channel.unary_stream(
          '/Datastore/replicator',
          request_serializer=Request1.SerializeToString,
          response_deserializer=Response1.FromString,
          )


  class DatastoreServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def put(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def replicator(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_DatastoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'put': grpc.unary_unary_rpc_method_handler(
            servicer.put,
            request_deserializer=Request.FromString,
            response_serializer=Response.SerializeToString,
        ),
        'get': grpc.unary_unary_rpc_method_handler(
            servicer.get,
            request_deserializer=Request.FromString,
            response_serializer=Response.SerializeToString,
        ),
        'replicator': grpc.unary_stream_rpc_method_handler(
            servicer.replicator,
            request_deserializer=Request1.FromString,
            response_serializer=Response1.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Datastore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaDatastoreServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def put(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def get(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def replicator(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaDatastoreStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def put(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    put.future = None
    def get(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    get.future = None
    def replicator(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()


  def beta_create_Datastore_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Datastore', 'get'): Request.FromString,
      ('Datastore', 'put'): Request.FromString,
      ('Datastore', 'replicator'): Request1.FromString,
    }
    response_serializers = {
      ('Datastore', 'get'): Response.SerializeToString,
      ('Datastore', 'put'): Response.SerializeToString,
      ('Datastore', 'replicator'): Response1.SerializeToString,
    }
    method_implementations = {
      ('Datastore', 'get'): face_utilities.unary_unary_inline(servicer.get),
      ('Datastore', 'put'): face_utilities.unary_unary_inline(servicer.put),
      ('Datastore', 'replicator'): face_utilities.unary_stream_inline(servicer.replicator),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Datastore_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Datastore', 'get'): Request.SerializeToString,
      ('Datastore', 'put'): Request.SerializeToString,
      ('Datastore', 'replicator'): Request1.SerializeToString,
    }
    response_deserializers = {
      ('Datastore', 'get'): Response.FromString,
      ('Datastore', 'put'): Response.FromString,
      ('Datastore', 'replicator'): Response1.FromString,
    }
    cardinalities = {
      'get': cardinality.Cardinality.UNARY_UNARY,
      'put': cardinality.Cardinality.UNARY_UNARY,
      'replicator': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Datastore', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
