# Encryption Script


## Encryption
Iinputs a text file location, reads the file, modifies all the characters in 
ASCII format, all values less than 100 it adds 96 with them, then with the key 
taken as input it adds 1 then 2 then 3 upto the key value consecutively with 
each ASCII value if it reaches the key number it re-initializes to 1 and continues the loop to modify the file.
finally it replaces the original file with encryptednumber text.
