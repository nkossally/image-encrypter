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

# IRREDUCIBLE = "00011011"
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

def hex_to_binary_string( hex_string ):
    int_value = int(hex_string, SIXTEEN)

    binary_string = format((int_value), '08b')

    # print("hex_to_binary_string")
    # print(hex_string)
    # print(binary_string)
    
    return binary_string

def add_8_bit_binary_arrays(arr_1, arr_2):
    print("add_8_bit_binary_arrays")
    print(arr_1)
    print(arr_2)

    sum = []

    for i in range(EIGHT):
        val_1 = arr_1[i] 
        val_2 = arr_2[i] 
        if (val_1 == 1 and val_2 == 0) or (val_1 == 0 and val_2 == 1):
            sum.append(1)
        else:
            sum.append(0)

    # print("sum")
    # print(arr_1)
    # print(arr_2)
    # print(sum)

    return sum

def multiply_binary_strings(str_1, str_2):
    num_arr_1 = list(map(int, str_1))
    num_arr_2 = list(map(int, str_2))

    # print("multiply_binary_strings")
    # print(num_arr_1)
    # print(num_arr_2)

    product = multiply_polynomials(num_arr_1, num_arr_2)      

    # print(product)      

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
            # print(i + j)
            result[i + j] += coeff1 * coeff2
            result[i + j] =  result[i + j] % 2
    
    # print(result)
    while(len(result) < EIGHT + 1):
        print("too small")
        result.insert(0, 0)


    # get last nine bits 
    # result = result[len(result) - 1 - EIGHT:]

    ninth_bit = result[len(result) - 1 - EIGHT]

    if ninth_bit == 1:
        print("too long")
        print(result)
        result = result[len(result)  - EIGHT:]
        print("after slicing")
        print(result)
        result = add_8_bit_binary_arrays(result, IRREDUCIBLE)
        print(result)
        return result

    # make it 8 bits
    result = result[len(result)  - EIGHT:]

    print(result)

    return result

def mix(matrix):
    transformed_matrix = []
    
    for i in range(FOUR):
        transformed_matrix.append([])

    for i in range(FOUR):
        row = list(map(num_to_binary_string, FORWARD_MATRIX[i]))
        print("row")
        print(row)

        for j in range(FOUR):
            col = [matrix[0][j], matrix[1][j], matrix[2][j], matrix[3][j]]
            col = map(hex_to_binary_string, col)
            product = multiply_binary_strings(col, row)


            transformed_matrix[i].append(product)

    result = []
    for i in range(len(transformed_matrix)):
        new_row = []
        old_row = transformed_matrix[i]
        for arr in old_row:
            new_row.append(binary_arr_to_hex(arr))
        
        result.append(new_row)

    print(transformed_matrix)
    print(result)

    return result


def binary_arr_to_hex(arr):
    str_arr = map(str, arr)
    return binary_to_hex("-".join(str_arr))

def binary_to_hex(binary_string):
    """Converts a binary string to a hexadecimal string.

    Args:
        binary_string: The binary string to convert.

    Returns:
        The hexadecimal string representation of the binary string, or None if the input is invalid.
    """
    if not isinstance(binary_string, str) or not all(bit in '01' for bit in binary_string):
        return None

    decimal_value = int(binary_string, 2)

    hex_string = hex(decimal_value)[2:]  # Remove the "0x" prefix

    return hex_string.upper() #Return uppercase for standard hex notation

