from six import *
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: riak_dt.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rriak_dt.proto\"\x85\x01\n\x08MapField\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12$\n\x04type\x18\x02 \x02(\x0e\x32\x16.MapField.MapFieldType\"E\n\x0cMapFieldType\x12\x0b\n\x07\x43OUNTER\x10\x01\x12\x07\n\x03SET\x10\x02\x12\x0c\n\x08REGISTER\x10\x03\x12\x08\n\x04\x46LAG\x10\x04\x12\x07\n\x03MAP\x10\x05\"\x98\x01\n\x08MapEntry\x12\x18\n\x05\x66ield\x18\x01 \x02(\x0b\x32\t.MapField\x12\x15\n\rcounter_value\x18\x02 \x01(\x12\x12\x11\n\tset_value\x18\x03 \x03(\x0c\x12\x16\n\x0eregister_value\x18\x04 \x01(\x0c\x12\x12\n\nflag_value\x18\x05 \x01(\x08\x12\x1c\n\tmap_value\x18\x06 \x03(\x0b\x32\t.MapEntry\"\xcf\x01\n\nDtFetchReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x0b\n\x03key\x18\x02 \x02(\x0c\x12\x0c\n\x04type\x18\x03 \x02(\x0c\x12\t\n\x01r\x18\x04 \x01(\r\x12\n\n\x02pr\x18\x05 \x01(\r\x12\x14\n\x0c\x62\x61sic_quorum\x18\x06 \x01(\x08\x12\x13\n\x0bnotfound_ok\x18\x07 \x01(\x08\x12\x0f\n\x07timeout\x18\x08 \x01(\r\x12\x15\n\rsloppy_quorum\x18\t \x01(\x08\x12\r\n\x05n_val\x18\n \x01(\r\x12\x1d\n\x0finclude_context\x18\x0b \x01(\x08:\x04true\"x\n\x07\x44tValue\x12\x15\n\rcounter_value\x18\x01 \x01(\x12\x12\x11\n\tset_value\x18\x02 \x03(\x0c\x12\x1c\n\tmap_value\x18\x03 \x03(\x0b\x32\t.MapEntry\x12\x11\n\thll_value\x18\x04 \x01(\x04\x12\x12\n\ngset_value\x18\x05 \x03(\x0c\"\x9a\x01\n\x0b\x44tFetchResp\x12\x0f\n\x07\x63ontext\x18\x01 \x01(\x0c\x12#\n\x04type\x18\x02 \x02(\x0e\x32\x15.DtFetchResp.DataType\x12\x17\n\x05value\x18\x03 \x01(\x0b\x32\x08.DtValue\"<\n\x08\x44\x61taType\x12\x0b\n\x07\x43OUNTER\x10\x01\x12\x07\n\x03SET\x10\x02\x12\x07\n\x03MAP\x10\x03\x12\x07\n\x03HLL\x10\x04\x12\x08\n\x04GSET\x10\x05\"\x1e\n\tCounterOp\x12\x11\n\tincrement\x18\x01 \x01(\x12\"&\n\x05SetOp\x12\x0c\n\x04\x61\x64\x64s\x18\x01 \x03(\x0c\x12\x0f\n\x07removes\x18\x02 \x03(\x0c\"\x16\n\x06GSetOp\x12\x0c\n\x04\x61\x64\x64s\x18\x01 \x03(\x0c\"\x15\n\x05HllOp\x12\x0c\n\x04\x61\x64\x64s\x18\x01 \x03(\x0c\"\xd1\x01\n\tMapUpdate\x12\x18\n\x05\x66ield\x18\x01 \x02(\x0b\x32\t.MapField\x12\x1e\n\ncounter_op\x18\x02 \x01(\x0b\x32\n.CounterOp\x12\x16\n\x06set_op\x18\x03 \x01(\x0b\x32\x06.SetOp\x12\x13\n\x0bregister_op\x18\x04 \x01(\x0c\x12\"\n\x07\x66lag_op\x18\x05 \x01(\x0e\x32\x11.MapUpdate.FlagOp\x12\x16\n\x06map_op\x18\x06 \x01(\x0b\x32\x06.MapOp\"!\n\x06\x46lagOp\x12\n\n\x06\x45NABLE\x10\x01\x12\x0b\n\x07\x44ISABLE\x10\x02\"@\n\x05MapOp\x12\x1a\n\x07removes\x18\x01 \x03(\x0b\x32\t.MapField\x12\x1b\n\x07updates\x18\x02 \x03(\x0b\x32\n.MapUpdate\"\x88\x01\n\x04\x44tOp\x12\x1e\n\ncounter_op\x18\x01 \x01(\x0b\x32\n.CounterOp\x12\x16\n\x06set_op\x18\x02 \x01(\x0b\x32\x06.SetOp\x12\x16\n\x06map_op\x18\x03 \x01(\x0b\x32\x06.MapOp\x12\x16\n\x06hll_op\x18\x04 \x01(\x0b\x32\x06.HllOp\x12\x18\n\x07gset_op\x18\x05 \x01(\x0b\x32\x07.GSetOp\"\xf1\x01\n\x0b\x44tUpdateReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0c\n\x04type\x18\x03 \x02(\x0c\x12\x0f\n\x07\x63ontext\x18\x04 \x01(\x0c\x12\x11\n\x02op\x18\x05 \x02(\x0b\x32\x05.DtOp\x12\t\n\x01w\x18\x06 \x01(\r\x12\n\n\x02\x64w\x18\x07 \x01(\r\x12\n\n\x02pw\x18\x08 \x01(\r\x12\x1a\n\x0breturn_body\x18\t \x01(\x08:\x05\x66\x61lse\x12\x0f\n\x07timeout\x18\n \x01(\r\x12\x15\n\rsloppy_quorum\x18\x0b \x01(\x08\x12\r\n\x05n_val\x18\x0c \x01(\r\x12\x1d\n\x0finclude_context\x18\r \x01(\x08:\x04true\"\x9b\x01\n\x0c\x44tUpdateResp\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\x0c\x12\x15\n\rcounter_value\x18\x03 \x01(\x12\x12\x11\n\tset_value\x18\x04 \x03(\x0c\x12\x1c\n\tmap_value\x18\x05 \x03(\x0b\x32\t.MapEntry\x12\x11\n\thll_value\x18\x06 \x01(\x04\x12\x12\n\ngset_value\x18\x07 \x03(\x0c\x42#\n\x17\x63om.basho.riak.protobufB\x08RiakDtPB')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'riak_dt_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.basho.riak.protobufB\010RiakDtPB'
  _MAPFIELD._serialized_start=18
  _MAPFIELD._serialized_end=151
  _MAPFIELD_MAPFIELDTYPE._serialized_start=82
  _MAPFIELD_MAPFIELDTYPE._serialized_end=151
  _MAPENTRY._serialized_start=154
  _MAPENTRY._serialized_end=306
  _DTFETCHREQ._serialized_start=309
  _DTFETCHREQ._serialized_end=516
  _DTVALUE._serialized_start=518
  _DTVALUE._serialized_end=638
  _DTFETCHRESP._serialized_start=641
  _DTFETCHRESP._serialized_end=795
  _DTFETCHRESP_DATATYPE._serialized_start=735
  _DTFETCHRESP_DATATYPE._serialized_end=795
  _COUNTEROP._serialized_start=797
  _COUNTEROP._serialized_end=827
  _SETOP._serialized_start=829
  _SETOP._serialized_end=867
  _GSETOP._serialized_start=869
  _GSETOP._serialized_end=891
  _HLLOP._serialized_start=893
  _HLLOP._serialized_end=914
  _MAPUPDATE._serialized_start=917
  _MAPUPDATE._serialized_end=1126
  _MAPUPDATE_FLAGOP._serialized_start=1093
  _MAPUPDATE_FLAGOP._serialized_end=1126
  _MAPOP._serialized_start=1128
  _MAPOP._serialized_end=1192
  _DTOP._serialized_start=1195
  _DTOP._serialized_end=1331
  _DTUPDATEREQ._serialized_start=1334
  _DTUPDATEREQ._serialized_end=1575
  _DTUPDATERESP._serialized_start=1578
  _DTUPDATERESP._serialized_end=1733
# @@protoc_insertion_point(module_scope)
