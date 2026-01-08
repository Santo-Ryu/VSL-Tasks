import base64

hexStr = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

def hex_to_base64(hex_string): 
    byte_data = bytes.fromhex(hex_string) # Convert hex string to bytes
    print(byte_data)
    
    base64_data = base64.b64encode(byte_data) # Encode bytes to base64
    print(base64_data)
    
    return base64_data.decode('utf-8') # Convert bytes to string

if __name__ == "__main__":
    base64Str = hex_to_base64(hexStr)
    print(f"flag: {{{base64Str}}}")
