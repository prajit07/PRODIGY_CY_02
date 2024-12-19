from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            decrypted_pixel = (b, g, r)
            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            decrypted_pixel = pixels[i, j]
            r, g, b = decrypted_pixel

            pixels[i, j] = (r, g, b)

    img.save(output_path)
    print("Image decrypted successfully!")

# Define the paths
path = input("Enter the directory path where you want to save the images: ")
input_image_path = input("Enter the full path to the input image: ")
#input_image_path = input_image_path.strip('"')  # Remove extra double quotes
encrypted_image_path = os.path.join(path, "encrypted.jpg")
decrypted_image_path = os.path.join(path, "decrypted.jpg")

# Run the program in a loop until the user chooses to exit
while True:
    choice = input("Do you want to encrypt or decrypt an image? (e/d) ")
    if choice.lower() == 'e':
        encrypt_image(input_image_path, encrypted_image_path, key=None)
        print("Image encrypted successfully!")
    elif choice.lower() == 'd':
        decrypt_image(encrypted_image_path, decrypted_image_path, key=None)
        print("Image decrypted successfully!")
    else:
        print("Invalid choice. Please try again.")
        continue

    choice = input("Do you want to continue? (y/n) ")
    if choice.lower() == 'n':
        break