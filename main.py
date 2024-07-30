from base64_encoder import base64

# penggunaan dengan teks
message = input("Masukkan Pesan : ")
b64 = base64(message, 'string')
encoded_output = b64.encode()
print("Encoded output: " + encoded_output)
b64.decode(encoded_output)

# penggunaan dengan gambar
image_file = 'image.png'
b64_image = base64(image_file, 'image')
encoded_image = b64_image.encode()
print("Encoded image output: " + encoded_image)
b64_image.decode(encoded_image)
