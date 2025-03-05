import time
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

from stable import forward_substitution, backwards_substitution
from shift_rows import forward_shift, backward_shift
from mix_column import forward_mix, backward_mix
from key_expansion import convert_32_char_hex_text_to_binary_matrix, handle_key_expansion_round
from utilities import xor_binary_arrays, convert_binary_matrix_to_hex_matrix, convert_image_to_matrix, binary_int_array_to_image, binary_int_matrix_to_binary_string_matrices, binary_string_matrices_to_binary_int_matrix, image_to_byte_array, binary_array_to_image, binary_string_arr_to_binary_string_matrices, binary_string_matrices_to_binary_string_arr
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Configuration       
cloudinary.config(
    cloud_name = "dhumr9ajv", 
    api_key = "897897225992447", 
    api_secret = "kzphOSXDte8CvQLQ5m6-YFyhQvo", # Click 'View API Keys' above to copy your API secret
    secure=True
)


key = "00001010101000011000101100000011001111000000111110110011001011011111101110011111100010110101010100110001100011011010100101110100"
hex_key = "0f1571c947d9e8590cb7add6af7f6798"
text = "0123456789abcdeffedcba9876543210"

decryption_key = [['b4', '8e', 'f3', '52'], ['ba', '98', '13', '4e'], [
    '7f', '4d', '59', '20'], ['86', '26', '18', '76']]

@app.route('/upload', methods = ['POST'])
@cross_origin()
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        upload_result = cloudinary.uploader.upload(file, public_id="897897225992447")
        print("upload result", upload_result["secure_url"])

        return jsonify({"message": "File uploaded successfully", "filename": filename}), 200
    else:
        return jsonify({"error": "Unsupported file type"}), 415

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
    # result = image_to_byte_array("cat.jpg")
    # binary_matrix = result[0]
    # width = result[1][0]
    # height = result[1][1]
    # str_matrices = binary_string_arr_to_binary_string_matrices(binary_matrix)
    # encrypted_str_matrices = list(map(encrypt_16_bytes, str_matrices ))    
    # flattened_arr = binary_string_matrices_to_binary_string_arr(encrypted_str_matrices)
    # binary_array_to_image(flattened_arr, width, height, "encrypted_image.png")
    # decrypted_str_matrices = list(map(decrypt_16_bytes,  encrypted_str_matrices ))
    # flattened_arr = binary_string_matrices_to_binary_string_arr(decrypted_str_matrices)
    # binary_array_to_image(flattened_arr, width, height, "decrypted_image.png")



    binary_matrices = convert_image_to_matrix()
    str_matrices = binary_int_matrix_to_binary_string_matrices(binary_matrices)
    encrypted_str_matrices = list(map(encrypt_16_bytes, str_matrices ))
    binary_int_arr = binary_string_matrices_to_binary_int_matrix(encrypted_str_matrices)
    binary_int_array_to_image(binary_int_arr, "encrypted_image.png")
    decrypted_str_matrices = list(map(decrypt_16_bytes,  encrypted_str_matrices ))
    binary_int_arr = binary_string_matrices_to_binary_int_matrix(decrypted_str_matrices)
    binary_int_array_to_image(binary_int_arr, "decrypted_image.png")


blarg()
