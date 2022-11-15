value_bin = "101"
value_int = int(value_bin, 2)
print(value_int)

value_hex = "2A"
value_int = int(value_hex, 16)
print(value_int)

value_hex = hex(value_int)
value_bin = bin(value_int)
print(value_hex, value_bin)


binary_bytes = b"0b101010"
binary_bytes_decoded = binary_bytes.decode()
print(binary_bytes)
print(binary_bytes_decoded)

# 0 - 0
# 1 - 1
# 10 - 2
# 11 - 3
# 100 - 4
# 101 - 5
