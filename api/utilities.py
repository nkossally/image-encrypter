from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from PIL import Image
import numpy as np

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



def convert_image_to_matrix():
    # Load the image
    image_path = 'cat.jpg'  # Replace with your image file path
    image = Image.open(image_path)

    # Convert to grayscale (this step makes the image easier to threshold)
    gray_image = image.convert('L')

    # Convert the grayscale image to a NumPy array
    gray_array = np.array(gray_image)

    # Apply a threshold to convert the grayscale image to binary
    # You can adjust the threshold value (here, it's 128) to get the desired result
    threshold = 128
    binary_matrix = (gray_array > threshold).astype(int)

    # Print the binary matrix
    print(binary_matrix)
    return binary_matrix




def convert_image_to_matrix_with_color_data():

    # Load the image
    image_path = 'cat.jpg'  # Replace with your image file path
    image = Image.open(image_path)


    # Convert the image to RGB (in case it's RGBA, CMYK, etc.)
    image = image.convert('RGB')

    # Convert the image to a NumPy array
    image_data = np.array(image)

    # Define a threshold to convert colors to binary (e.g., 128)
    threshold = 128

    # Apply thresholding to each color channel (R, G, B)
    binary_matrix = (image_data > threshold).astype(int)

    # The result is a 3D matrix of shape (height, width, 3)
    # where the third dimension represents [R_binary, G_binary, B_binary] for each pixel

    # Show the binary matrix (optional)
    return binary_matrix

def binary_int_array_to_image(binary_matrix):
    numpy_binary_matrix = np.array(binary_matrix)  # Ensure it's a NumPy array

    numpy_binary_matrix = numpy_binary_matrix.astype(np.uint8)  # Convert to unsigned 8-bit integers

    # Convert binary matrix to an 8-bit image (0=black, 255=white)
    image_data = numpy_binary_matrix * 255  # Multiply by 255 to make it a grayscale image

    # Convert the image data to a PIL Image
    image = Image.fromarray(image_data.astype(np.uint8))

    # Save or display the image
    image.show()  # To display the image
    image.save('binary_image.png')  # Save the image to a file

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

def rgb_binary_int_matrix_to_binary_string_matrices(binary_int_matrix):
    result = []
    for color in range(3):
        for row in binary_int_matrix:
            color_segment_row = [elem[0]  for elem in row]
            for i in range(EIGHT):
                binary_str_matrix = []
                for j in range(FOUR):
                    str_row = []
                    for k in range(FOUR):
                        idx = i * FOUR * FOUR * EIGHT + j * EIGHT * FOUR + k * EIGHT
                        sub_arr = list(map(str, color_segment_row[idx: idx + EIGHT]))
                        sub_arr_str = "".join(sub_arr)
                        str_row.append(sub_arr_str)
                    binary_str_matrix.append(str_row)
                result.append(binary_str_matrix)

    return result

def convert_binary_str_matrix_to_str(binary_str_matrix):
    def flatten_arr(arr):
        return "".join(arr)

    joined_matrix = list(map(flatten_arr, binary_str_matrix))
    joined_string = flatten_arr(joined_matrix)
    return joined_string
