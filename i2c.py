from pyi2c import I2C

# Create i2c
BUS_N = 0  # 0 or 1 or 2. Change this to yours
i2c = I2C(BUS_N)

ADDR = 0x38  # Change this to yours

# Return:
#
#     {StatusCode.success: 0}
#     {StatusCode.ready: 1}
#     {StatusCode.fail: 9}

print(i2c.status_code)
# => {StatusCode: 1}

# To get the value, use .value
print(i2c.status_code.value)
# => 1

if i2c.status_code.value == 1:
    print('ready')

# scan() Scan all I2C devices on the same BUS. Return list of integer (address in byte)
print(i2c.scan())
#     00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f
# 00: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 30: -- -- -- -- -- -- -- -- 38 -- -- -- -- -- -- --
# 40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 50: -- -- -- -- -- -- -- -- -- -- 5a -- -- -- -- --
# 60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 70: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 80: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# [56, 90]

# write(ADDR, data). Return nothing
# data can be a byte or list of bytes.
WRITE0 = 0x00  # Change this to yours
i2c.write(ADDR, WRITE0)

# or write multi bytes, up to 64 bytes
WRITE1 = 0x01  # Change this to yours
i2c.write(ADDR, [WRITE0, WRITE1])

# read(ADDR, byte_size=1)
# Return integer (a byte), or list of integers (bytes) if byte_size >= 0
# byte_size can be empty (default is 1)
read_data = i2c.read(ADDR)
# or set length of reading bytes
byte_size = 2
read_data = i2c.read(ADDR, byte_size)
print(len(read_data))  # 2

# writeread(ADDR, data, byte_size=1)
# Return integer (a byte), or list of integer (bytes) if byte_size >= 0
# data can be a byte or list of bytes.
# byte_size can be empty (default is 1)

# First write and read rapidly one byte
read_data = i2c.writeread(ADDR, WRITE0)

# These also work
read_data = i2c.writeread(ADDR, [WRITE0, WRITE1])
read_data = i2c.writeread(ADDR, [WRITE0, WRITE1], byte_size)

# I2CDevice(bus_n, addr)
# It is extension of I2C, but contains a I2C device's address. So it is not need to write address any more after declare.
from pyi2c import I2CDevice

BUS_N = 0
ADDR = 0x38

aht10 = I2CDevice(BUS_N, ADDR)
# status_code
# As the same as status_code in I2C.

# write(data)
# As the same as write(addr, data) in I2C, but does not need address.
# read(byte_size=1)
# As the same as read(addr, byte_size) in I2C, but does not need address.
# writeread(data, byte_size=1)
# As the same as writeread(addr, data, byte_size=1) in I2C, but does not need address.

# getBit(byte, bin_n, bin_m=-1)
# Return integer (a bit or bits)
# bin_n should be >= 0
# bin_m can be empty (default is -1 but will overwrote with bin_n)
# bin_n or bin_m can be larger than byte's size
from pyi2c import getBit

byte = 0x5a  # Any byte data
print(bin(byte))  # '0b1011010'

# Get bit #n of byte
print(getBit(byte, 0))  # 0
print(getBit(byte, 1))  # 1

# Get multi bits from #n to #m of byte
print(getBit(byte, 4, 3))  # 3 = 0b10
print(getBit(byte, 3, 4))  # 3 = 0b10, the same as previous
# Recommend usage:
if getBit(byte, 4) == 0b1:
    print('hoge')
# 'hoge'
