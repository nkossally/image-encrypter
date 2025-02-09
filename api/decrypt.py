from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES

# Function to decrypt an image file
def decrypt_image(input_file, output_file, key):
    with open(input_file, "rb") as file:
        iv = file.read(16)  # First 16 bytes are the IV
        encrypted_data = file.read()

    # Create AES cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove padding
    unpadded_data = unpad(decrypted_data, AES.block_size)

    # Save the decrypted image
    with open(output_file, "wb") as file:
        file.write(unpadded_data)

    print("Decryption successful. Decrypted file saved as:", output_file)

# Example usage
# decrypt_image("encrypted.img", "decrypted.jpg", key)
