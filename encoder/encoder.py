import random

print("# Encrypte your file content")

file_path = input("Enter filepath : ")
file_path = file_path.strip()

# Open the file to read
with open(file_path, 'r') as file:
    text = file.read()

key = int(input("Enter encryption key : "))

code = ""
ascii = 0
ascii_list = []
bias = 1

for char in text:
    if ord(char) < 100:
        ascii = ord(char) + 96
    else:
        ascii = ord (char)
    if bias > key:
        bias = 1
    ascii = ascii + bias
    bias = bias + 1
    ascii_list.append(str(ascii))

for x in range(len(text)):
    code = code + ascii_list[x]

header = random.randint(1000,10000)
header = str(header)
code = header + code

# Wtiting modified file by creating name_encrypted file
# file_path = file_path.replace(".", "_encrypted.")
if key < 10:
    key = "00" + str(key)
elif key < 100:
    key = "0" + str(key)
heading = "# Decryption key is {}\n\n"
heading = heading.format(key)
with open(file_path, 'w') as file:
    # Write content to the file
    file.write(heading)
    file.write(code)
is_ascii = "All ASCII Character = {}"

print(f"\n\033[0;31;47mNOTICE:\n\033[1;37;40mThe file has been encrypted.\n")
print(is_ascii.format(text.isascii()))
