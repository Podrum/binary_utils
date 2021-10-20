r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team.

 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""

import struct

class BinaryConverter:
    @staticmethod
    def read_byte(data: bytes) -> int:
        return struct.unpack("b", data)[0]
    
    @staticmethod
    def write_byte(value: int) -> bytes:
        return struct.pack("b", value)
    
    @staticmethod
    def read_unsigned_byte(data: bytes) -> int:
        return struct.unpack("B", data)[0]
    
    @staticmethod
    def write_unsigned_byte(value: int) -> bytes:
        return struct.pack("B", value)
    
    @staticmethod
    def read_bool(data: bytes) -> bool:
        return struct.unpack("?", data)[0]
    
    @staticmethod
    def write_bool(value: bool) -> bytes:
        return struct.pack("?", value)
    
    @staticmethod
    def read_short_be(data: bytes) -> int:
        return struct.unpack(">h", data)[0]
    
    @staticmethod
    def write_short_be(value: int) -> bytes:
        return struct.pack(">h", value)
    
    @staticmethod
    def read_unsigned_short_be(data: bytes) -> int:
        return struct.unpack(">H", data)[0]
    
    @staticmethod
    def write_unsigned_short_be(value: int) -> bytes:
        return struct.pack(">H", value)
    
    @staticmethod
    def read_short_le(data: bytes) -> int:
        return struct.unpack("<h", data)[0]
    
    @staticmethod
    def write_short_le(value: int) -> bytes:
        return struct.pack("<h", value)
    
    @staticmethod
    def read_unsigned_short_le(data: bytes) -> int:
        return struct.unpack("<H", data)[0]
    
    @staticmethod
    def write_unsigned_short_le(value: int) -> bytes:
        return struct.pack("<H", value)
    
    @staticmethod
    def read_triad_be(data: bytes) -> int:
        return struct.unpack(">i", b"\x00" + data)[0]
    
    @staticmethod
    def write_triad_be(value: int) -> bytes:
        return struct.pack(">i", value)[1:4]
    
    @staticmethod
    def read_unsigned_triad_be(data: bytes) -> int:
        return struct.unpack(">I", b"\x00" + data)[0]
    
    @staticmethod
    def write_unsigned_triad_be(value: int) -> bytes:
        return struct.pack(">I", value)[1:4]
    
    @staticmethod
    def read_triad_le(data: bytes) -> int:
        return struct.unpack("<i", data + b"\x00")[0]
    
    @staticmethod
    def write_triad_le(value: int) -> bytes:
        return struct.pack("<i", value)[:3]
    
    @staticmethod
    def read_unsigned_triad_le(data: bytes) -> int:
        return struct.unpack("<I", data + b"\x00")[0]
    
    @staticmethod
    def write_unsigned_triad_le(value: int) -> bytes:
        return struct.pack("<I", value)[:3]
    
    @staticmethod
    def read_int_be(data: bytes) -> int:
        return struct.unpack(">i", data)[0]
    
    @staticmethod
    def write_int_be(value: int) -> bytes:
        return struct.pack(">i", value)
    
    @staticmethod
    def read_unsigned_int_be(data: bytes) -> int:
        return struct.unpack(">I", data)[0]
    
    @staticmethod
    def write_unsigned_int_be(value: int) -> bytes:
        return struct.pack(">I", value)
    
    @staticmethod
    def read_int_le(data: bytes) -> int:
        return struct.unpack("<i", data)[0]
    
    @staticmethod
    def write_int_le(value: int) -> bytes:
        return struct.pack("<i", value)
    
    @staticmethod
    def read_unsigned_int_le(data: bytes) -> int:
        return struct.unpack("<I", data)[0]
    
    @staticmethod
    def write_unsigned_int_le(value: int) -> bytes:
        return struct.pack("<I", value)
    
    @staticmethod
    def read_long_be(data: bytes) -> int:
        return struct.unpack(">q", data)[0]
    
    @staticmethod
    def write_long_be(value: int) -> bytes:
        return struct.pack(">q", value)
    
    @staticmethod
    def read_unsigned_long_be(data: bytes) -> int:
        return struct.unpack(">Q", data)[0]
    
    @staticmethod
    def write_unsigned_long_be(value: int) -> bytes:
        return struct.pack(">Q", value)
    
    @staticmethod
    def read_long_le(data: bytes) -> int:
        return struct.unpack("<q", data)[0]
    
    @staticmethod
    def write_long_le(value: int) -> bytes:
        return struct.pack("<q", value)
    
    @staticmethod
    def read_unsigned_long_le(data: bytes) -> int:
        return struct.unpack("<Q", data)[0]
    
    @staticmethod
    def write_unsigned_long_le(value: int) -> bytes:
        return struct.pack("<Q", value)
    
    @staticmethod
    def read_float_be(data: bytes) -> int:
        return struct.unpack(">f", data)[0]
    
    @staticmethod
    def write_float_be(value: int) -> bytes:
        return struct.pack(">f", value)
    
    @staticmethod
    def read_float_le(data: bytes) -> int:
        return struct.unpack("<f", data)[0]
    
    @staticmethod
    def write_float_le(value: int) -> bytes:
        return struct.pack("<f", value)

    @staticmethod
    def read_double_be(data: bytes) -> int:
        return struct.unpack(">d", data)[0]
    
    @staticmethod
    def write_double_be(value: int) -> bytes:
        return struct.pack(">d", value)
    
    @staticmethod
    def read_double_le(data: bytes) -> int:
        return struct.unpack("<d", data)[0]
    
    @staticmethod
    def write_double_le(value: int) -> bytes:
        return struct.pack("<d", value)
