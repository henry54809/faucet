# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/shared_constants.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/shared_constants.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"forch/proto/shared_constants.proto\"\x8d\x01\n\x05State\"\x83\x01\n\x05State\x12\x0b\n\x07unknown\x10\x00\x12\n\n\x06\x62roken\x10\x01\x12\n\n\x06\x61\x63tive\x10\x02\x12\x0b\n\x07\x64\x61maged\x10\x03\x12\x08\n\x04\x64own\x10\x04\x12\x0b\n\x07healthy\x10\x05\x12\x0c\n\x08inactive\x10\x06\x12\x10\n\x0cinitializing\x10\x07\x12\t\n\x05split\x10\x08\x12\x06\n\x02up\x10\t\"Y\n\tLacpState\"L\n\tLacpState\x12\x0b\n\x07\x64\x65\x66\x61ult\x10\x00\x12\x11\n\x04none\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x08\n\x04init\x10\x01\x12\n\n\x06\x61\x63tive\x10\x03\x12\t\n\x05noact\x10\x05\"N\n\x08\x44VAState\"B\n\x05State\x12\x0b\n\x07initial\x10\x00\x12\x13\n\x0funauthenticated\x10\x01\x12\n\n\x06static\x10\x02\x12\x0b\n\x07\x64ynamic\x10\x03\x62\x06proto3')
)



_STATE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='State.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='broken', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='active', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='damaged', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='down', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='healthy', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='inactive', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='initializing', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='split', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='up', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=49,
  serialized_end=180,
)
_sym_db.RegisterEnumDescriptor(_STATE_STATE)

_LACPSTATE_LACPSTATE = _descriptor.EnumDescriptor(
  name='LacpState',
  full_name='LacpState.LacpState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='none', index=1, number=-1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='init', index=2, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='active', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='noact', index=4, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=195,
  serialized_end=271,
)
_sym_db.RegisterEnumDescriptor(_LACPSTATE_LACPSTATE)

_DVASTATE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='DVAState.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='initial', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='unauthenticated', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='static', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='dynamic', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=285,
  serialized_end=351,
)
_sym_db.RegisterEnumDescriptor(_DVASTATE_STATE)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=180,
)


_LACPSTATE = _descriptor.Descriptor(
  name='LacpState',
  full_name='LacpState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LACPSTATE_LACPSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=271,
)


_DVASTATE = _descriptor.Descriptor(
  name='DVAState',
  full_name='DVAState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DVASTATE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=351,
)

_STATE_STATE.containing_type = _STATE
_LACPSTATE_LACPSTATE.containing_type = _LACPSTATE
_DVASTATE_STATE.containing_type = _DVASTATE
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['LacpState'] = _LACPSTATE
DESCRIPTOR.message_types_by_name['DVAState'] = _DVASTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(
  DESCRIPTOR = _STATE,
  __module__ = 'forch.proto.shared_constants_pb2'
  # @@protoc_insertion_point(class_scope:State)
  ))
_sym_db.RegisterMessage(State)

LacpState = _reflection.GeneratedProtocolMessageType('LacpState', (_message.Message,), dict(
  DESCRIPTOR = _LACPSTATE,
  __module__ = 'forch.proto.shared_constants_pb2'
  # @@protoc_insertion_point(class_scope:LacpState)
  ))
_sym_db.RegisterMessage(LacpState)

DVAState = _reflection.GeneratedProtocolMessageType('DVAState', (_message.Message,), dict(
  DESCRIPTOR = _DVASTATE,
  __module__ = 'forch.proto.shared_constants_pb2'
  # @@protoc_insertion_point(class_scope:DVAState)
  ))
_sym_db.RegisterMessage(DVAState)


# @@protoc_insertion_point(module_scope)
