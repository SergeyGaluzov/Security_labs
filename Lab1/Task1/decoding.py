import base64
import numpy as np


def get_symbol_pairs(string):
    indexes = np.arange(1, len(string), 2)
    string_list = np.array(list(string))
    even_symbols = string_list[indexes]
    odd_symbols = string_list[indexes - 1]
    return np.core.defchararray.add(odd_symbols, even_symbols).tolist()


file_path = "Lab1\\Task0\\ciphered_text.txt"
with open(file_path) as f:
    text = f.read()

hex_text_representation = hex(int(text, 2))[2:]

encoded_text = "".join(list(
    map(lambda x: chr(int(x, 16)), get_symbol_pairs(hex_text_representation))
))
decoded_text = base64.b64decode(encoded_text)\
    .decode('utf-8').replace('’', '\'')

print(decoded_text)

output_file_path = "Lab1\\Task0\\decoded_text_with_tasks.txt"
with open(output_file_path, "w") as text_file:
    text_file.write(decoded_text)
