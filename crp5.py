def encrypt_affine(msg, a, b):
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    
    if not (0 < a < 26 and 0 <= b < 26 and gcd(a, 26) == 1):
        return "Invalid values of a and/or b."
    
    return ''.join([chr(((a * (ord(c.upper()) - ord('A')) + b) % 26) + ord('A')) if c.isalpha() else c for c in msg])

msg = input("Enter the plain text: ")
ciphertext = encrypt_affine(msg, 5, 7)
print("plaintext:", msg)
print("Ciphertext:",ciphertext)
