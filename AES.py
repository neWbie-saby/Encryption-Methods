from Crypto.Cipher import AES

key = "Sixteen byte key"
plain = "Secrets 16 bytes"
Cipher = AES.new(key)
ciphertext = Cipher.encrypt(plain)
print("AES Encoded: ",ciphertext.hex())     #.encode("hex"))

plaintext = Cipher.decrypt(ciphertext)
print("Decoded: ",plaintext.decode())
