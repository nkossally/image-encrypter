SIXTEEN = 16
FOUR = 4

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
