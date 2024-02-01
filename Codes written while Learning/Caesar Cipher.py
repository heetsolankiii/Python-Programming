def encrypt(message, key):
  result = ""
  for i in range(len(message)):
    char = message[i]
    if char.isupper():
      result += chr((ord(char) + key - 65) % 26 + 65)
    else:
      result += chr((ord(char) + key - 97) % 26 + 97)
  return result

message = input("Enter a message: ")
key = int(input("Enter key: "))

print(f"Message: {message}")
print(f"Key: {key}")
print(f"Encrypted message: {encrypt(message, key)}")