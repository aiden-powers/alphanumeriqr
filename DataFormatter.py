import json
import random

def sample_data(size):
    data = ""
    for i in range(size):
        data += random.choice("01")
    return data

def load_encoding_list(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def encode_binary(binary_str, encoding_list):
    encoded_str = ""
    for i in range(0, len(binary_str), 5):
        chunk = binary_str[i:i + 5]
        for encoding in encoding_list:
            if chunk in encoding:
                encoded_str += encoding[chunk]
                break
    return encoded_str

def decode_binary(encoded_str, encoding_list):
    decoded_str = ""
    for char in encoded_str:
        for encoding in encoding_list:
            if char in encoding.values():
                decoded_str += list(encoding.keys())[list(encoding.values()).index(char)]
                break
    return decoded_str