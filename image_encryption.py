from PIL import Image

def encrypt_image(image_path, output_path, operation, value):
    image = Image.open(image_path)
    encrypted_image = image.copy()

    for y in range(encrypted_image.height):
        for x in range(encrypted_image.width):
            pixel = encrypted_image.getpixel((x, y))

            if operation == "swap":
                encrypted_image.putpixel((x, y), encrypted_image.getpixel((y, x)))
            elif operation == "add":
                encrypted_image.putpixel((x, y), tuple(map(lambda x: min(255, x + value), pixel)))
            elif operation == "subtract":
                encrypted_image.putpixel((x, y), tuple(map(lambda x: max(0, x - value), pixel)))

    encrypted_image.save(output_path)

def decrypt_image(encrypted_image_path, output_path, operation, value):
    encrypted_image = Image.open(encrypted_image_path)
    decrypted_image = encrypted_image.copy()

    for y in range(decrypted_image.height):
        for x in range(decrypted_image.width):
            pixel = decrypted_image.getpixel((x, y))

            if operation == "swap":
                decrypted_image.putpixel((x, y), decrypted_image.getpixel((y, x)))
            elif operation == "add":
                decrypted_image.putpixel((x, y), tuple(map(lambda x: x - value, pixel)))
            elif operation == "subtract":
                decrypted_image.putpixel((x, y), tuple(map(lambda x: x + value, pixel)))

    decrypted_image.save(output_path)

if __name__ == "__main__":
    print("Image Encryption and Decryption")

    operation = input("Enter the operation (swap/add/subtract): ")
    value = int(input("Enter the value: "))

    image_path = input("Enter the path of the image to encrypt: ")
    encrypted_image_path = input("Enter the path to save the encrypted image: ")
    encrypt_image(image_path, encrypted_image_path, operation, value)

    encrypted_image_path = input("Enter the path of the encrypted image to decrypt: ")
    decrypted_image_path = input("Enter the path to save the decrypted image: ")
    decrypt_image(encrypted_image_path, decrypted_image_path, operation, value)
