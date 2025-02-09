from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# Function to encrypt an image file
def encrypt_image(input_file, output_file, key):
    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)  

    # Create AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Read the image data
    with open(input_file, "rb") as file:
        image_data = file.read()
    
    print("image datat")
    print(type(image_data))

    

    # print(image_data)
    
    binary_string = utf8_to_binary(image_data)
    print("binary_string")
    print(binary_string)
    print(len(binary_string))


    # Pad the data to be a multiple of 16 bytes
    padded_data = pad(image_data, AES.block_size)
    print("padded data")
    print(type(padded_data))


    padded_binary_string = utf8_to_binary(padded_data)
    print("padded binary string")
    print(padded_binary_string)
    print(len(padded_binary_string))


    # print(padded_data)

    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)

    # Save the IV + encrypted data to the output file
    with open(output_file, "wb") as file:
        file.write(iv + encrypted_data)

    print("Encryption successful. Encrypted file saved as:", output_file)

def utf8_to_binary(text):
    # binary_string = ''.join(format(byte, '08b') for byte in text.encode('utf-8'))
    binary_string = ''.join(format(byte, '08b') for byte in text)

    return binary_string


