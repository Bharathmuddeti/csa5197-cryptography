P = "hello everyone"
lst1 = [chr(i) for i in range(97, 123)]

plaintext = [lst1.index(char) for char in P if char in lst1]
cipher = [(x + 1) % 26 for x in plaintext]

print("".join([lst1[i] for i in cipher]))

