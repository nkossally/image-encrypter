import time
from flask import Flask

from encrypt import encrypt_image
from decrypt import decrypt_image
from stable import forward_transformation, backwards_transformation
from shift_rows import forward_shift, backward_shift
from mix_column import forward_mix, backward_mix

app = Flask(__name__)

matrix = [
    ["EA", "04", "65", "85"],
    ["83", "45", "5D", "96"],
    ["5C", "33", "98", "B0"],
    ["F0", "2D", "AD", "C5"],
]

matrix_2 = [
    ["87", "F2", "4D", "97"],
    ["EC", "6E", "4C", "90"],
    ["4A", "C3", "46", "E7"],
    ["8C", "D8", "95", "A6"]
]

matrix_3 = [
    ["87", "F2", "4D", "97"],
    ["6E", "4C", "90", "EC"],
    ["46", "E7", "4A", "C3"],
    ["A6", "8C", "D8", "95"]
]

matrix_4 = [
    ['47', '40', 'A3', '4C'], 
    ['37', 'D4', '70', '9F'], 
    ['94', 'E4', '3A', '42'], 
    ['ED', 'A5', 'A6', 'BC']
]

@app.route('/time')
def blarg():
    transformed = forward_mix(matrix_3)
    # transformed = backward_mix(matrix_4)

    # Example usage
    # key = "10111001111010101100111011001101"
    # encoded_key = key.encode('utf-8')

    # encrypt_image("cat.jpg", "encrypted.img", encoded_key)
    # print("encoded key")
    # print(type(encoded_key))
    # print(encoded_key)

    # decrypt_image("encrypted.img", "decrypted.jpg", encoded_key)

blarg()