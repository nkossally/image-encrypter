SIXTEEN = 16

key = "00001010101000011000101100000011001111000000111110110011001011011111101110011111100010110101010100110001100011011010100101110100"

S_BOX = [
  ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
  ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
  ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
  ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
  ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
  ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
  ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
  ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
  ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
  ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
  ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
  ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
  ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
  ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
  ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
  ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]

ROUND_CONSTANTS = [
    "01000000",
    "02000000",
    "04000000",
    "08000000",
    "10000000",
    "20000000",
    "40000000",
    "80000000",
    "1B000000",
    "36000000"
]

def convert_key_to_arr(key):
    bytes_arr = [key[i:i+8] for i in range(0, len(key), 8)]
    bytes_arr = [bytes_arr[i:i+4] for i in range(0, len(bytes_arr), 4)]

    # words = list(map(group_by_four_bytes, words))
    print(bytes_arr)
    return bytes_arr

def handle_round(bytes_arr, round):
    return

def g_function(bytes_arr, round):
    new_words = bytes_arr[:1] + bytes_arr[0 : 1]
    transformed_bytes = []
    for i in range(len(bytes_arr)):
        row = bytes_arr[i]
        new_row = []
        for j in range(len(row)):
            binary_str = row[j]
            lookup_row = int(binary_str, 2)
            lookup_col = int(binary_str, 2)
            hex_str = S_BOX[lookup_row][lookup_col]
            transformed_binary_str = hex_to_binary_string(hex_str)
            new_row.append(transformed_binary_str)

        transformed_bytes.append(new_row)

    return transformed_bytes


def xor(binary_str_1, binary_str_2):
    sum = ""
    for i in range(len(binary_str_1)):
        if binary_str_1[i] != binary_str_2[i]:
            sum += "1"
        else:
            sum += "0"
    return sum

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

def hex_to_binary_string( hex_string ):
    int_value = int(hex_string, SIXTEEN)

    binary_string = format((int_value), '08b')
    
    return binary_string
