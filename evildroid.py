a = [-92, 12, 23, 115, 84, 48, -125, -66, 40, 59, 105, 63, 19, 29, -93, -67, 92, 119, 69, -62, 127, 35, 114, 85, 117, -5, -34, -94, -73, -97, 41, -78, 59, 13, -116, -103, -51, 53, -112, 25, -30, -76, 109, -52, -114, 118, -80, 0]
ciphertext = bytes([x & 255 for x in a])
print("ciphertext:", ciphertext.hex())

a = [122, 61, 66, 31, 11, 0, 33, 84, 16, 68, 56, 77, 61, 66, 31, 127, 66, 31, 127, 42, 27, 3, 9, 17, 0, 33, 84, 31, 11, 31, 11, 31]
key = bytes([x & 255 for x in a])
print("key:", key.hex())

from Crypto.Cipher import AES

cipher = AES.new(key, AES.MODE_ECB)
print("plain text:", cipher.decrypt(ciphertext))
