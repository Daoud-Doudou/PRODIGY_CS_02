from PIL import Image
import numpy as np



def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    print(pixels)
    encrypted_pixels = np.clip(pixels[:, :, ::-2] + key, 0, 255)
    print(encrypted_pixels)
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    # Convertir en mode compatible si nécessaire
    if encrypted_image.mode in ('LA', 'RGBA'):
        encrypted_image = encrypted_image.convert('RGB')
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    print(pixels)
    pixels_origin = np.clip(pixels[:, :, ::-2] - key, 0, 255)
    print(pixels_origin)
    decrypted_image = Image.fromarray(pixels_origin.astype('uint8'))
    if decrypted_image.mode in ('LA', 'RGBA'):
        decrypted_image = decrypted_image.convert('RGB')
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    while True:
        print("\nTool for Encrypting and Decrypting Pictures:")
        print("1. Encrypt picture")
        print("2. Decrypt picture")
        print("3. Exit")
        choice = input("Choose 1/2/3: ")

        if choice == "1":
            image_path = input("Enter the path to the image to encrypt: ")
            output_path = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter the key to use for encryption: "))
            encrypt_image(image_path, key, output_path)

        elif choice == "2":
            image_path = input("Enter the path to the image to decrypt: ")
            output_path = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the key used for encryption: "))
            decrypt_image(image_path, key, output_path)
        
        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()