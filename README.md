XOR File Encryption / Decryption Tool

This is a simple Python-based XOR encryption and decryption utility. It allows you to encrypt or decrypt any file using a user-provided XOR key. Since XOR is a symmetric operation, running the program again with the same key will decrypt the data.

The tool supports multiple output formats, making it useful for both general file protection and embedding encrypted data into source code.

Features

Encrypts and decrypts files using XOR

Supports both plaintext and hexadecimal keys

Automatically repeats the key if it is shorter than the input

Multiple output formats:

raw – writes encrypted bytes directly to a file

python – outputs a Python bytes array

c – outputs a C unsigned char array with length

Handles binary files safely

Clear error handling for invalid input, keys, or file paths

How It Works

The input file is read as raw bytes.

The key is parsed as either:

a UTF-8 string, or

a hexadecimal byte sequence (e.g. 0xAA BB CC).

Each byte of the input is XORed with the corresponding byte of the key.

The key repeats automatically if it is shorter than the data.

The result is written in the selected output format.

Because XOR is reversible, the same process is used for both encryption and decryption.

Usage

Run the script and follow the prompts:

python xor_encrypt.py


You will be asked for:

Input file path

Output file path

XOR key

Output format (raw, python, or c)

Example hex key inputs:

0x414243

41 42 43

Example string key:

mysecretkey

Output Formats

raw
Writes encrypted bytes directly to the output file.

python
Outputs a Python bytes([...]) array suitable for embedding in scripts.

c
Outputs a C unsigned char array with a comment showing its length.
