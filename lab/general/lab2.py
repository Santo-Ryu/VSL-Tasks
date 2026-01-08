# Hex practice
hex_str = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Tranfer hex -> bytes
flag_bytes = bytes.fromhex(hex_str)

# Check type
print(f"Flag: \n{flag_bytes}\n")
print(f"Type: \n{type(flag_bytes)}\n")
print(f"Bytes value of flag: \n{list(flag_bytes)}\n")

# Tranfer bytes value -> escape (debug)
def bytes_to_escape(b): 
	return ''.join(f'\\x{byte:02x}' for byte in b)

print(f"Bytes to escape of flag: \n{bytes_to_escape(flag_bytes)}\n")

# Decode from bytes -> string
final_flag = flag_bytes.decode()
print(f"Type after decode: \n{type(final_flag)}\n")

# Final flag
print(f"Flag: \n{final_flag}\n")

"""
Vậy bài toán trên cho mã hex, để đưa về string đọc được thì phải 
chuyển từ hex -> bytes -> decoding (bằng bảng mã ascii) -> string
còn nếu hex -> bytes bằng bytes.fromhex() thì chỉ lấy ra bytes 
do printable ánh xạ với quy tắc ascii nên sẽ hiển thị bytes dưới dạng ascii để dễ đọc, 
nếu muốn hiển thị bytes 0-255 thì dùng list để hiển thị ra

function bytes_to_escape() để hiển thị bytes dưới dạng escape \x00-\xff => đúng bản chất của bytes
"""