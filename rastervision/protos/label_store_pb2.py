# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/label_store.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/label_store.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_pb=_b('\n%rastervision/protos/label_store.proto\x12\trv.protos\x1a\x1cgoogle/protobuf/struct.proto\"\xe1\x03\n\x10LabelStoreConfig\x12\x12\n\nstore_type\x18\x01 \x02(\t\x12\r\n\x03uri\x18\x02 \x01(\tH\x00\x12i\n\"semantic_segmentation_raster_store\x18\x03 \x01(\x0b\x32;.rv.protos.LabelStoreConfig.SemanticSegmentationRasterStoreH\x00\x12\x30\n\rcustom_config\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x1a\xf6\x01\n\x1fSemanticSegmentationRasterStore\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x12\n\x03rgb\x18\x02 \x01(\x08:\x05\x66\x61lse\x12_\n\rvector_output\x18\x03 \x03(\x0b\x32H.rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore.VectorOutput\x1aQ\n\x0cVectorOutput\x12\x12\n\x07\x64\x65noise\x18\x01 \x01(\x05:\x01\x30\x12\r\n\x03uri\x18\x02 \x01(\t:\x00\x12\x0c\n\x04mode\x18\x03 \x02(\t\x12\x10\n\x08\x63lass_id\x18\x04 \x02(\x05\x42\x14\n\x12label_store_config')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE_VECTOROUTPUT = _descriptor.Descriptor(
  name='VectorOutput',
  full_name='rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore.VectorOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='denoise', full_name='rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore.VectorOutput.denoise', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uri', full_name='rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore.VectorOutput.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore.VectorOutput.mode', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_id', full_name='rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore.VectorOutput.class_id', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=542,
)

_LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE = _descriptor.Descriptor(
  name='SemanticSegmentationRasterStore',
  full_name='rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rgb', full_name='rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore.rgb', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vector_output', full_name='rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore.vector_output', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE_VECTOROUTPUT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=542,
)

_LABELSTORECONFIG = _descriptor.Descriptor(
  name='LabelStoreConfig',
  full_name='rv.protos.LabelStoreConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='store_type', full_name='rv.protos.LabelStoreConfig.store_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uri', full_name='rv.protos.LabelStoreConfig.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='semantic_segmentation_raster_store', full_name='rv.protos.LabelStoreConfig.semantic_segmentation_raster_store', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_config', full_name='rv.protos.LabelStoreConfig.custom_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='label_store_config', full_name='rv.protos.LabelStoreConfig.label_store_config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=83,
  serialized_end=564,
)

_LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE_VECTOROUTPUT.containing_type = _LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE
_LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE.fields_by_name['vector_output'].message_type = _LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE_VECTOROUTPUT
_LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE.containing_type = _LABELSTORECONFIG
_LABELSTORECONFIG.fields_by_name['semantic_segmentation_raster_store'].message_type = _LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE
_LABELSTORECONFIG.fields_by_name['custom_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LABELSTORECONFIG.oneofs_by_name['label_store_config'].fields.append(
  _LABELSTORECONFIG.fields_by_name['uri'])
_LABELSTORECONFIG.fields_by_name['uri'].containing_oneof = _LABELSTORECONFIG.oneofs_by_name['label_store_config']
_LABELSTORECONFIG.oneofs_by_name['label_store_config'].fields.append(
  _LABELSTORECONFIG.fields_by_name['semantic_segmentation_raster_store'])
_LABELSTORECONFIG.fields_by_name['semantic_segmentation_raster_store'].containing_oneof = _LABELSTORECONFIG.oneofs_by_name['label_store_config']
_LABELSTORECONFIG.oneofs_by_name['label_store_config'].fields.append(
  _LABELSTORECONFIG.fields_by_name['custom_config'])
_LABELSTORECONFIG.fields_by_name['custom_config'].containing_oneof = _LABELSTORECONFIG.oneofs_by_name['label_store_config']
DESCRIPTOR.message_types_by_name['LabelStoreConfig'] = _LABELSTORECONFIG

LabelStoreConfig = _reflection.GeneratedProtocolMessageType('LabelStoreConfig', (_message.Message,), dict(

  SemanticSegmentationRasterStore = _reflection.GeneratedProtocolMessageType('SemanticSegmentationRasterStore', (_message.Message,), dict(

    VectorOutput = _reflection.GeneratedProtocolMessageType('VectorOutput', (_message.Message,), dict(
      DESCRIPTOR = _LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE_VECTOROUTPUT,
      __module__ = 'rastervision.protos.label_store_pb2'
      # @@protoc_insertion_point(class_scope:rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore.VectorOutput)
      ))
    ,
    DESCRIPTOR = _LABELSTORECONFIG_SEMANTICSEGMENTATIONRASTERSTORE,
    __module__ = 'rastervision.protos.label_store_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.LabelStoreConfig.SemanticSegmentationRasterStore)
    ))
  ,
  DESCRIPTOR = _LABELSTORECONFIG,
  __module__ = 'rastervision.protos.label_store_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.LabelStoreConfig)
  ))
_sym_db.RegisterMessage(LabelStoreConfig)
_sym_db.RegisterMessage(LabelStoreConfig.SemanticSegmentationRasterStore)
_sym_db.RegisterMessage(LabelStoreConfig.SemanticSegmentationRasterStore.VectorOutput)


# @@protoc_insertion_point(module_scope)
