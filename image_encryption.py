from PIL import Image

def encrypt_image(input_path, output_path, key):
    # Load the image and convert to RGB mode
    image = Image.open(input_path).convert('RGB')
    pixels = image.load()

    # Encrypt the image by modifying pixel values
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            # Apply different operations to each channel
            r_encrypted = (r + key) % 256
            g_encrypted = (g + key) % 256  # Use addition instead of multiplication
            b_encrypted = (b ^ key) % 256
            pixels[i, j] = (r_encrypted, g_encrypted, b_encrypted)

    # Save the encrypted image
    image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    # Load the image and convert to RGB mode
    image = Image.open(input_path).convert('RGB')
    pixels = image.load()

    # Decrypt the image by reversing the pixel modifications
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            # Reverse the operations applied during encryption
            r_decrypted = (r - key) % 256
            g_decrypted = (g - key) % 256  # Use subtraction instead of reversing multiplication
            b_decrypted = (b ^ key) % 256
            pixels[i, j] = (r_decrypted, g_decrypted, b_decrypted)

    # Save the decrypted image
    image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

# Example usage
input_image_path = 'input_image.png'  # Ensure this file exists in your working directory
encrypted_image_path = 'encrypted_image.png'
decrypted_image_path = 'decrypted_image.png'
encryption_key = 50  # You can choose any integer as the key

encrypt_image(input_image_path, encrypted_image_path, encryption_key)
decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)
