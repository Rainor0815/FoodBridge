# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: locate.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'locate.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0clocate.proto\"4\n\rvolunteerInfo\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x13\n\x0buserAddress\x18\x02 \x01(\t\"x\n\tinputBody\x12\x11\n\tproductId\x18\x01 \x01(\t\x12\x16\n\x0eproductAddress\x18\x02 \x01(\t\x12\x19\n\x11productHubAddress\x18\x03 \x01(\t\x12%\n\rvolunteerList\x18\x04 \x03(\x0b\x32\x0e.volunteerInfo\"B\n\x0cresponseBody\x12\x11\n\tproductId\x18\x01 \x01(\t\x12\x10\n\x08userList\x18\x02 \x03(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t29\n\x06locate\x12/\n\x10getFilteredUsers\x12\n.inputBody\x1a\r.responseBody\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'locate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VOLUNTEERINFO']._serialized_start=16
  _globals['_VOLUNTEERINFO']._serialized_end=68
  _globals['_INPUTBODY']._serialized_start=70
  _globals['_INPUTBODY']._serialized_end=190
  _globals['_RESPONSEBODY']._serialized_start=192
  _globals['_RESPONSEBODY']._serialized_end=258
  _globals['_LOCATE']._serialized_start=260
  _globals['_LOCATE']._serialized_end=317
# @@protoc_insertion_point(module_scope)
