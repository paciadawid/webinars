a = "101"
b = "100"
a_int = int(a, 2)
b_int = int(b, 2)

bit_and = a_int & b_int
bit_or = a_int | b_int
bit_xor = a_int ^ b_int
bit_not = ~a_int
bit_shift_left = a_int << 2
print(bit_and)


hex_text = "7369656d61"

print(ord("a"))
print(chr(110))

ascii_text = bytes.fromhex(hex_text).decode()
print(ascii_text)

new_hex = ascii_text.encode().hex()
print(new_hex)