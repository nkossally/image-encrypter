import time
from flask import Flask

from encrypt import encrypt_image
from decrypt import decrypt_image
from stable import forward_substitution, backwards_substitution
from shift_rows import forward_shift, backward_shift
from mix_column import forward_mix, backward_mix
from key_expansion import convert_binary_key_to_arr, convert_32_char_hex_text_to_binary_matrix, handle_key_expansion, handle_key_expansion_round
from utilities import xor, hex_to_eight_bit_binary_string, hex_to_four_bit_binary_string, xor_binary_arrays, convert_binary_matrix_to_hex_matrix, convert_hex_matrix_to_binary_matrix, convert_image_to_binary_matrices, convert_image_to_matrix, binary_int_array_to_image, binary_int_matrix_to_binary_string_matrices, binary_string_matrices_to_binary_int_matrix, image_to_byte_array, binary_array_to_image, binary_string_arr_to_binary_string_matrices, binary_string_matrices_to_binary_string_arr

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

key = "00001010101000011000101100000011001111000000111110110011001011011111101110011111100010110101010100110001100011011010100101110100"
hex_key = "0f1571c947d9e8590cb7add6af7f6798"
text = "0123456789abcdeffedcba9876543210"

decryption_key = [['b4', '8e', 'f3', '52'], ['ba', '98', '13', '4e'], [
    '7f', '4d', '59', '20'], ['86', '26', '18', '76']]


@app.route('/time')
def encrypt_16_bytes(curr_text_binary_arr):

    key_binary_arr = convert_32_char_hex_text_to_binary_matrix(hex_key)
    curr_text_binary_arr = xor_binary_arrays(
        curr_text_binary_arr, key_binary_arr)

    for i in range(10):
        curr_text_binary_arr = forward_substitution(curr_text_binary_arr)
        curr_text_binary_arr = forward_shift(curr_text_binary_arr)
        if i != 9:
            curr_text_binary_arr = forward_mix(curr_text_binary_arr)
        key_binary_arr = handle_key_expansion_round(key_binary_arr, i)
        key_hex_arr = convert_binary_matrix_to_hex_matrix(key_binary_arr)
        curr_text_binary_arr = xor_binary_arrays(
            curr_text_binary_arr, key_binary_arr)
    return curr_text_binary_arr


def decrypt_16_bytes(curr_text_binary_arr):

    round_keys = []
    key_binary_arr = convert_32_char_hex_text_to_binary_matrix(hex_key)

    # round_keys.insert(0, key_binary_arr)

    for i in range(10):
        round_keys.insert(0, key_binary_arr)
        key_binary_arr = handle_key_expansion_round(key_binary_arr, i)
        # key_hex_arr = convert_binary_matrix_to_hex_matrix(round_key

    curr_text_binary_arr = xor_binary_arrays(
        curr_text_binary_arr, key_binary_arr)

    for i in range(10):
        curr_text_binary_arr = backward_shift(curr_text_binary_arr)
        curr_text_binary_arr = backwards_substitution(curr_text_binary_arr)
        curr_text_binary_arr = xor_binary_arrays(
            curr_text_binary_arr, round_keys[i])

        if i != 9:
            curr_text_binary_arr = backward_mix(curr_text_binary_arr)

    return curr_text_binary_arr


def blarg():
    result = image_to_byte_array("cat.jpg")
    binary_matrix = result[0]
    width = result[1][0]
    height = result[1][1]
    str_matrices = binary_string_arr_to_binary_string_matrices(binary_matrix)
    encrypted_str_matrices = list(map(encrypt_16_bytes, str_matrices ))    
    flattened_arr = binary_string_matrices_to_binary_string_arr(encrypted_str_matrices)
    binary_array_to_image(flattened_arr, width, height, "encrypted_image.png")
    decrypted_str_matrices = list(map(decrypt_16_bytes,  encrypted_str_matrices ))
    flattened_arr = binary_string_matrices_to_binary_string_arr(decrypted_str_matrices)
    binary_array_to_image(flattened_arr, width, height, "decrypted_image.png")



    # binary_matrices = convert_image_to_matrix()
    # str_matrices = binary_int_matrix_to_binary_string_matrices(binary_matrices)
    # encrypted_str_matrices = list(map(encrypt_16_bytes, str_matrices ))
    # binary_int_arr = binary_string_matrices_to_binary_int_matrix(encrypted_str_matrices)
    # binary_int_array_to_image(binary_int_arr, "encrypted_image.png")
    # decrypted_str_matrices = list(map(decrypt_16_bytes,  encrypted_str_matrices ))
    # binary_int_arr = binary_string_matrices_to_binary_int_matrix(decrypted_str_matrices)
    # binary_int_array_to_image(binary_int_arr, "decrypted_image.png")


blarg()
