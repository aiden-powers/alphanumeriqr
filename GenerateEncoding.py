import string
import json

encoding_list = []
alphanumeric = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

# Define the bit lengths and their corresponding ranges
bit_lengths = [(5, 32), (4, 16), (3, 8), (2, 4), (1, 2)]

for bits, count in bit_lengths:
    for i in range(count):
        encoding_list.append({f"{i:0{bits}b}": alphanumeric.pop(0)})

with open("encoding_alphanumeric.json", "w") as file:
    json.dump(encoding_list, file, indent=4)