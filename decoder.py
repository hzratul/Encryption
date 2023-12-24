# Read encrypted file
file_path = input("Enter filepath : \n")
file_path = file_path.strip()

# Open the file in read mode ('r')
with open(file_path, 'r') as file:
    # Read the entire content of the file
    file_content = file.read()

# Refine the content of the file
file_content = file_content.replace("# Decryption key is", "")
file_content = file_content.replace(" ", "")
file_content = file_content.replace("\n", "")
file_content = file_content.strip()

key = file_content[:3]
code = file_content[7:] + key
key = int(key)

is_digit = code.isdigit()



spaced_code = code
i = 0
for n in range(1, int(len(code) + (len(code)/3 - 1))):
    if (n % 3 == 0.0):
        index = int(n + i)
        spaced_code = spaced_code[:index] + " " + spaced_code[index:]
        i = i + 1

spaced_code = spaced_code.strip()
raw_ascii = spaced_code.split(" ")

# Removing bias value from ascii values 
bias = len(raw_ascii) % key

for x in range(len(raw_ascii)):
    x = -x - 1
    if bias == 0:
        bias = key
    raw_ascii[x] = int(raw_ascii[x]) - bias
    if(raw_ascii[x] > 127):
        raw_ascii[x] = raw_ascii[x] - 96
    bias = bias - 1

# Converting refined ascii to chars
output = ""
for x in range(len(raw_ascii)):
    if x != (len(raw_ascii) - 1):
        output = output + chr(raw_ascii[x])






# replacing the decrypted code in the file
with open(file_path, 'w') as file:
    # Write content to the file
    file.write(output)
print(f"\n\033[0;31;47mNOTICE:\n\033[1;37;40mThe file \033[1;32;40m '{file_path}' \033[1;37;40m has been decrypted")
print(f"Processed code is numeric = {is_digit}")



