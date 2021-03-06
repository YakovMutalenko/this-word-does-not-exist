# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import wordservice_pb2 as wordservice__pb2


class WordServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DefineWord = channel.unary_unary(
        '/endpoints.word_service.WordService/DefineWord',
        request_serializer=wordservice__pb2.DefineWordRequest.SerializeToString,
        response_deserializer=wordservice__pb2.DefineWordResponse.FromString,
        )
    self.WordFromDefinition = channel.unary_unary(
        '/endpoints.word_service.WordService/WordFromDefinition',
        request_serializer=wordservice__pb2.WordFromDefinitionRequest.SerializeToString,
        response_deserializer=wordservice__pb2.WordFromDefinitionResponse.FromString,
        )
    self.GenerateWord = channel.unary_unary(
        '/endpoints.word_service.WordService/GenerateWord',
        request_serializer=wordservice__pb2.GenerateWordRequest.SerializeToString,
        response_deserializer=wordservice__pb2.GenerateWordResponse.FromString,
        )


class WordServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DefineWord(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WordFromDefinition(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenerateWord(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WordServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DefineWord': grpc.unary_unary_rpc_method_handler(
          servicer.DefineWord,
          request_deserializer=wordservice__pb2.DefineWordRequest.FromString,
          response_serializer=wordservice__pb2.DefineWordResponse.SerializeToString,
      ),
      'WordFromDefinition': grpc.unary_unary_rpc_method_handler(
          servicer.WordFromDefinition,
          request_deserializer=wordservice__pb2.WordFromDefinitionRequest.FromString,
          response_serializer=wordservice__pb2.WordFromDefinitionResponse.SerializeToString,
      ),
      'GenerateWord': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateWord,
          request_deserializer=wordservice__pb2.GenerateWordRequest.FromString,
          response_serializer=wordservice__pb2.GenerateWordResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'endpoints.word_service.WordService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
