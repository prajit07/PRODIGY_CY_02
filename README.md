**# PRODIGY_CY_02
Pixel Manipulation for Image Encryption**
This Python script performs pixel manipulation for image encryption. It reads an image, modifies its pixel values using a simple encryption algorithm, and saves the encrypted image. The script also provides functionality to decrypt the image back to its original form.

**Features**
Encrypt Image: Modify pixel values to encrypt the image.

Decrypt Image: Restore the original image from the encrypted version.

Simple XOR Encryption: Uses XOR operation for encryption and decryption.

**Requirements**
Python 3.x

Pillow library (PIL fork)

**Installation**
**Clone the Repository:**

bash

git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name

**Install Dependencies:**

bash
pip install pillow
**Usage**
Encrypt an Image
To encrypt an image, use the encrypt_image function. Provide the path to the input image, the path to save the encrypted image, and an encryption key.
