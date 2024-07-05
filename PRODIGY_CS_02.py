

from PIL import Image
def encrypt_image(image_path):
    
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Example: swap red and blue channels
            pixels[i, j] = (b, g, r)
  
    encrypted_image_path = 'encrypted_image.png'
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")
    return encrypted_image_path
def decrypt_image(encrypted_image_path):

    encrypted_img = Image.open(encrypted_image_path)
    pixels = encrypted_img.load()
    width, height = encrypted_img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Example: swap red and blue channels back to original
            pixels[i, j] = (b, g, r)

    decrypted_image_path = 'decrypted_image.png'
    encrypted_img.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")
    return decrypted_image_path

original_image_path =r'D:\New folder\Data-Encryption-Descryption-1024x631.jpg'

encrypted_image_path = encrypt_image(original_image_path)
decrypted_image_path = decrypt_image(encrypted_image_path)

