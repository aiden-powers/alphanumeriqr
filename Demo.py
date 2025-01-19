import qrcode

from DataFormatter import sample_data, encode_binary, load_encoding_list, decode_binary

data = sample_data(512) # 512 bits of random data

qrcode.make(data).save("raw.png")
print("Raw: ", data, "\n")

encoded_output = encode_binary(data, load_encoding_list('encoding_alphanumeric.json'))
qrcode.make(encoded_output).save("encoded.png")
print("Encoded: ", encoded_output, "\n")

print("Decoded: ", decode_binary(encoded_output, load_encoding_list('encoding_alphanumeric.json')))
print("\nMatch: ", data == decode_binary(encoded_output, load_encoding_list('encoding_alphanumeric.json')))

encoded = input("Scan the encoded QR code yourself and decode the data here: ")
print("\nDecoded: ", decode_binary(encoded, load_encoding_list('encoding_alphanumeric.json')))

print("\nMatch: ", data == decode_binary(encoded, load_encoding_list('encoding_alphanumeric.json')))