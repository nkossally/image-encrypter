from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from PIL import Image
import numpy as np
import math
import io
from io import BytesIO
import cloudinary
import cloudinary.uploader
import secrets

# Configuration       
cloudinary.config(
    cloud_name = "dhumr9ajv", 
    api_key = "897897225992447", 
    api_secret = "kzphOSXDte8CvQLQ5m6-YFyhQvo", # Click 'View API Keys' above to copy your API secret
    secure=True
)


SIXTEEN = 16
FOUR = 4
EIGHT = 8

def xor_binary_arrays(arr_1, arr_2):
    transformed_matrix = []
    for i in range(len(arr_1)):
        new_row = []
        for j in range(len(arr_1[0])):
            binary_str_1 = arr_1[i][j]
            binary_str_2 = arr_2[i][j]
            sum = xor(binary_str_1, binary_str_2)
            new_row.append(sum)
        
        transformed_matrix.append(new_row)
    
    return transformed_matrix

def xor(binary_str_1, binary_str_2):
    sum = ""
    for i in range(len(binary_str_1)):
        if binary_str_1[i] != binary_str_2[i]:
            sum += "1"
        else:
            sum += "0"
    return sum

def convert_hex_matrix_to_binary_matrix(matrix):
    transformed_matrix = []

    for i in range(len(matrix)):
        new_row = []
        for hex_str in matrix[i]:
            half_byte_1 = hex_str[0]
            half_byte_2 = hex_str[1]
            # binary_str = hex_to_four_bit_binary_string(half_byte_1) + hex_to_four_bit_binary_string(half_byte_2)
            binary_str = hex_to_eight_bit_binary_string(hex_str)

            new_row.append(binary_str)
        transformed_matrix.append(new_row)

    return transformed_matrix

def hex_to_eight_bit_binary_string( hex_string ):
    int_value = int(hex_string, SIXTEEN)

    binary_string = format((int_value), '08b')
    
    return binary_string

def hex_to_four_bit_binary_string( hex_string ):
    int_value = int(hex_string, SIXTEEN)

    binary_string = format((int_value), '04b')
    
    return binary_string

def convert_binary_arr_to_hex_arr(binary_arr):
    transformed_arr= []

    for binary_str in binary_arr:
        half_byte_1 = binary_str[0: FOUR]
        half_byte_2 = binary_str[FOUR :]
        hex_str = binary_to_hex_string(half_byte_1) + binary_to_hex_string(half_byte_2)
        if len(hex_str) == 4:
            hex_str = hex_str[1] + hex_str[3]
        transformed_arr.append(hex_str)

    return transformed_arr

def convert_binary_matrix_to_hex_matrix(matrix):
    transformed_matrix = []

    for i in range(len(matrix)):
        new_row = []
        for binary_string in matrix[i]:
            byte_1 = binary_string[0: FOUR]
            byte_2 = binary_string[FOUR :]
            hex_str = binary_to_hex_string(byte_1) + binary_to_hex_string(byte_2)
            if len(hex_str) == 4:
                hex_str = hex_str[1] + hex_str[3]

            new_row.append(hex_str)
        transformed_matrix.append(new_row)

    return transformed_matrix

def binary_to_hex_string( binary_string ):
    int_value = int(binary_string, 2)

    hex_string = hex(int_value)[2:]
    
    return hex_string

# Function to encrypt an image file
def convert_image_to_binary_matrices(input_file):

    # Read the image data
    with open(input_file, "rb") as file:
        image_data = file.read()  
    # Pad the data to be a multiple of 16 bytes
    padded_data = pad(image_data, AES.block_size)

    binary_string = utf8_to_binary(padded_data)
    binary_matrices = []

    for i in range(0, int(len(binary_string) / 128), 128):
        binary_matrix = []
        for j in range(0, 128, 32):
            row = []
            for k in range(0, 4):
                idx = i * 128 + j * 32 + 8 * k 
                row.append(binary_string[idx : idx + 8])
            binary_matrix.append(row)
        binary_matrices.append(binary_matrix)

    return binary_matrices


def utf8_to_binary(text):
    # binary_string = ''.join(format(byte, '08b') for byte in text.encode('utf-8'))
    binary_string = ''.join(format(byte, '08b') for byte in text)

    return binary_string



def convert_image_to_matrix(file):
    # Load the image
    image = Image.open(file)

    # Convert to grayscale (this step makes the image easier to threshold)
    gray_image = image.convert('L')

    # Convert the grayscale image to a NumPy array
    gray_array = np.array(gray_image)

    # Apply a threshold to convert the grayscale image to binary
    # You can adjust the threshold value (here, it's 128) to get the desired result
    threshold = 128
    binary_matrix = (gray_array > threshold).astype(int)

    return binary_matrix


def binary_int_array_to_image(binary_matrix, file_save_path):
    numpy_binary_matrix = np.array(binary_matrix)  # Ensure it's a NumPy array

    numpy_binary_matrix = numpy_binary_matrix.astype(np.uint8)  # Convert to unsigned 8-bit integers

    # Convert binary matrix to an 8-bit image (0=black, 255=white)
    image_data = numpy_binary_matrix * 255  # Multiply by 255 to make it a grayscale image
    print("image_data", image_data)

    # Convert the image data to a PIL Image
    image = Image.fromarray(image_data.astype(np.uint8))

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")  # You can change format if needed
    buffered.seek(0)

    upload_result = cloudinary.uploader.upload(buffered, public_id="897897225992447")
    print("upload result", upload_result["secure_url"])

    # # Save or display the image
    # image.show()  # To display the image
    # image.save(file_save_path)  # Save the image to a file
    return {"url": upload_result["secure_url"]}


def binary_int_matrix_to_binary_string_matrices(binary_int_matrix):
    result = []
    for row in binary_int_matrix:
        for i in range(EIGHT):
            binary_str_matrix = []
            for j in range(FOUR):
                str_row = []
                for k in range(FOUR):
                    idx = i * FOUR * FOUR * EIGHT + j * EIGHT * FOUR + k * EIGHT
                    sub_arr = list(map(str, row[idx: idx + EIGHT]))
                    sub_arr_str = "".join(sub_arr)
                    str_row.append(sub_arr_str)
                binary_str_matrix.append(str_row)
            result.append(binary_str_matrix)

    return result


def binary_string_matrices_to_binary_int_matrix(binary_str_matrices):
    result = []
    for i in range(0, len(binary_str_matrices), EIGHT):
        string = ""
        for j in range(EIGHT):
            if i + j < len(binary_str_matrices):
                string += convert_binary_str_matrix_to_str(binary_str_matrices[i + j])
        arr = list(map(int, list(string)))
        result.append(arr)
    return result


def image_to_byte_array(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    height, width, channels = img_array.shape
    binary_strings = []
    for row in img_array:
        for pixel in row:
            for channel_value in pixel:
                binary_string = bin(channel_value)[2:].zfill(8)  # Ensure 8 bits
                binary_strings.append(binary_string)
    return binary_strings, (width, height)


def binary_array_to_image(binary_strings, width, height, file_save_path):
    """
    Reconstructs an image from an array of binary strings and dimensions.

    Args:
        binary_strings (list): An array of binary strings representing the image data.
        dimensions (tuple): The original image dimensions (width, height).

    Returns:
        Image.Image: A PIL Image object representing the reconstructed image.
    """
    total_pixels = width * height
    if len(binary_strings) != total_pixels * 3:
        print("should be error", len(binary_strings), width * height)
        # raise ValueError("The number of binary strings does not match the image dimensions.")

    img_array = np.zeros((height, width, 3), dtype=np.uint8)
    index = 0
    for y in range(height):
        for x in range(width):
            for c in range(3):
                if index < len(binary_strings):
                    binary_string = binary_strings[index]
                    img_array[y, x, c] = int(binary_string, 2)
                    index += 1
                else:
                    img_array[y, x, c] = int("00000000", 2)


    img = Image.fromarray(img_array)
    img.show()
    img.save(file_save_path)  # Save the image to a file


def binary_string_arr_to_binary_string_matrices(binary_int_matrix):
    matrices = []
    num_matrices = math.floor(len(binary_int_matrix)/(FOUR * FOUR))
    for i in range(0, num_matrices, FOUR * FOUR ):
        matrix = []
        for j in range(FOUR):
            arr = []
            for k in range(FOUR):
                idx = i * FOUR * FOUR + j * FOUR + k
                if idx < len(binary_int_matrix):
                    arr.append(binary_int_matrix[idx])
                else:
                    arr.append("00000000")
            matrix.append(arr)
        matrices.append(matrix)

    return matrices


def binary_string_matrices_to_binary_string_arr(binary_matrices):
    result = [ ]
    for matrix in binary_matrices:
        for row in matrix:
            result += row
    return result

def convert_binary_str_matrix_to_str(binary_str_matrix):
    def flatten_arr(arr):
        return "".join(arr)

    joined_matrix = list(map(flatten_arr, binary_str_matrix))
    joined_string = flatten_arr(joined_matrix)
    return joined_string

def generate_key():
    hex_string = secrets.token_hex(16)  
    return hex_string
