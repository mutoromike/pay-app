import base64

def encode_data(data):
    encoded_data = base64.b64encode(data.encode("utf-8"))
    encoded_str = str(encoded_data, "utf-8")
    return encoded_str