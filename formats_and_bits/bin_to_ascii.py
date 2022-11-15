binary_bytes = b"01101001 00100000 01101100 01101001 01101011 01100101 00100000 01110000 01100001 01101110 01100011 01100001 01101011 01100101 01110011"
binary_parsed = binary_bytes.decode().replace(" ", "")
hex_value = hex(int(binary_parsed, 2))
string_value = bytes.fromhex(hex_value[2:]).decode()
print(string_value)