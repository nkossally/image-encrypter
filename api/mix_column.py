import numpy as np

FOUR = 4
SIXTEEN = 16
EIGHT = 8

FORWARD_MATRIX = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

BACKWARD_MATRIX = [
    [14, 11, 13, 9],
    [9, 14, 11, 13],
    [13, 9, 14, 11],
    [11, 13, 9, 14]
]


IRREDUCIBLES = [
    [0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
]


IRREDUCIBLE = [0, 0, 0, 1, 1, 0, 1, 1]

def string_to_int_array(s):
  """Splits a string of digits into an array of integers.

  Args:
    s: The string of digits.

  Returns:
    A list of integers.
  """
  return [int(digit) for digit in s]

def num_to_binary_string( num ):
    binary_string = format(num, '08b')

    return binary_string

def hex_to_binary_string_backwards( hex_string ):
    print("hex_to_binary_string_backwards")
    print(hex_string)

    int_value_1 = int(hex_string[0], SIXTEEN)
    int_value_2 = int(hex_string[1], SIXTEEN)

    binary_string = format((int_value_1), '04b') + format((int_value_2), '04b')
    
    print(binary_string)

    return binary_string

def hex_to_binary_string( hex_string ):
    int_value = int(hex_string, SIXTEEN)

    binary_string = format((int_value), '08b')
    
    return binary_string

def add_8_bit_binary_arrays(arr_1, arr_2):

    sum = []

    for i in range(EIGHT):
        val_1 = arr_1[i] 
        val_2 = arr_2[i] 
        if (val_1 == 1 and val_2 == 0) or (val_1 == 0 and val_2 == 1):
            sum.append(1)
        else:
            sum.append(0)

    return sum

def multiply_binary_strings(str_1, str_2):
    num_arr_1 = list(map(int, str_1))
    num_arr_2 = list(map(int, str_2))

    product = multiply_polynomials(num_arr_1, num_arr_2)      

    return product

def multiply_polynomials(poly1, poly2):
    """
    Multiplies two polynomials represented as lists of coefficients.

    Args:
        poly1: List of coefficients for the first polynomial.
        poly2: List of coefficients for the second polynomial.

    Returns:
        A list of coefficients representing the product polynomial.
    """
    result_degree = len(poly1) + len(poly2) - 2
    result = [0] * (result_degree + 1)


    for i, coeff1 in enumerate(poly1):
        for j, coeff2 in enumerate(poly2):
            result[i + j] += coeff1 * coeff2
            result[i + j] =  result[i + j] % 2

    for num in range(EIGHT + 1, EIGHT +  len(IRREDUCIBLES) + 1):
        if len(result) >= num:
            idx = len(result) - num
            irreducibles_idx = num - EIGHT - 1
            if result[idx] == 1:
                print("num")
                print(num)

                print("idx")
                print(idx)
                print("irreducible idx")
                print(irreducibles_idx)
                last_8_bits = result[len(result)  - EIGHT:]
                last_8_bits = add_8_bit_binary_arrays(last_8_bits, IRREDUCIBLES[irreducibles_idx])
                result = result[0: len(result)  - EIGHT] + last_8_bits
                # result = add_8_bit_binary_arrays(result, IRREDUCIBLES[irreducibles_idx])

    

    # ninth_bit = result[len(result) - 1 - EIGHT]
    # tenth_bit = result[len(result) - 2 - EIGHT]
    # eleventh_bit = result[len(result) - 3 - EIGHT]

    # if len(result) >= 9 and ninth_bit == 1:
    #     last_8_bits = result[len(result)  - EIGHT:]
    #     last_8_bits = add_8_bit_binary_arrays(last_8_bits, IRREDUCIBLES[0])
    #     result = result[0: len(result)  - EIGHT] + last_8_bits
    
    # if len(result) >= 10 and tenth_bit == 1:
    #     last_8_bits = result[len(result)  - EIGHT:]
    #     last_8_bits = add_8_bit_binary_arrays(last_8_bits, IRREDUCIBLES[1])
    #     result = result[0: len(result)  - EIGHT] + last_8_bits
    # if len(result) > 9 and tenth_bit == 1:
    #     result = result[len(result)  - EIGHT:]
    #     result = add_8_bit_binary_arrays(result, IRREDUCIBLES[0])

    # make it 8 bits
    if len(result) > 8:
        result = result[len(result) - EIGHT:]

    return result

def backward_mix(matrix):
    transformed_matrix = []
    
    for i in range(FOUR):
        transformed_matrix.append([])

    for i in range(FOUR):
        row = list(map(num_to_binary_string, BACKWARD_MATRIX[i]))
        print(row)

        for j in range(FOUR):
            col = [matrix[0][j], matrix[1][j], matrix[2][j], matrix[3][j]]
            col = list(map(hex_to_binary_string_backwards, col))


            sum =  [0] * (EIGHT)
            for k in range(FOUR):

                product = multiply_binary_strings(col[k], row[k])
                sum = add_8_bit_binary_arrays(sum, product)


            print(sum)
            first_dig = binary_arr_to_hex_arr(sum[0 : FOUR])
            second_dig = binary_arr_to_hex_arr(sum[FOUR:])
            transformed_matrix[i].append(first_dig + second_dig)

    print(transformed_matrix)
    return transformed_matrix

def forward_mix(matrix ):
    transformed_matrix = []
    
    for i in range(FOUR):
        transformed_matrix.append([])

    for i in range(FOUR):
        row = list(map(num_to_binary_string, FORWARD_MATRIX[i]))
        print(row)

        for j in range(FOUR):
            col = [matrix[0][j], matrix[1][j], matrix[2][j], matrix[3][j]]
            col = list(map(hex_to_binary_string, col))

            sum =  [0] * (EIGHT)
            for k in range(FOUR):

                product = multiply_binary_strings(col[k], row[k])
                sum = add_8_bit_binary_arrays(sum, product)


            print(sum)
            first_dig = binary_arr_to_hex_arr(sum[0 : FOUR])
            second_dig = binary_arr_to_hex_arr(sum[FOUR:])
            transformed_matrix[i].append(first_dig + second_dig)

    print(transformed_matrix)
    return transformed_matrix


def binary_arr_to_hex_arr(arr):
    str_arr = map(str, arr)
    return binary_str_to_hex_str("".join(str_arr))

def binary_str_to_hex_str(binary_string):
    """Converts a binary string to a hexadecimal string.

    Args:
        binary_string: The binary string to convert.

    Returns:
        The hexadecimal string representation of the binary string, or None if the input is invalid.
    """
    # if not isinstance(binary_string, str) or not all(bit in '01' for bit in binary_string):
    #     return None

    decimal_value = int(binary_string, 2)

    hex_string = hex(decimal_value)[2:]  # Remove the "0x" prefix

    return hex_string.upper() #Return uppercase for standard hex notation

