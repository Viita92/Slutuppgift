import argparse
import sys

def parse_args() -> argparse.Namespace:

    """Prompt the user for file paths, XOR key, and output format.

    Returns:
        argparse.Namespace: User-provided input file, output file, key,
        and output format ("raw", "python", or "c").
    """
    
    # This lets the user specify input/output files, key, and format when running the script.

    # User adds Inputfile to encrypt/decrypted file

    inputfile = input("Enter input file path: ")

    # User sets destination for encrypted/decrypted file to be created

    outfile = input("Enter output file path: ")

    # XOR key

    key = input("Enter XOR key: ")

    # Able to add format of output, default set to raw

    format_choice = input("Enter output format (raw/python/c) [default: raw]: ").strip().lower()
    
    
    if format_choice not in ["raw", "python", "c"]:
        format_choice = "raw"
        

    return argparse.Namespace(
        inputfile=inputfile,
        outfile=outfile,
        key=key,
        format=format_choice
        )
    

def is_hex_like(s: str) -> bool:

    """Return True if the string appears to be hexadecimal data."""

    # Check if input looks like hexadecimal (0x or aa bb cc dd)
    # Removes spaces and handles optional prefix.

    s_clean = s.strip().lower()
    if s_clean.startswith("0x"):
        s_clean = s_clean[2:]
    s_clean = s_clean.replace(" ", "")
    if not s_clean:
        return False
    
    #Trying to convert to integer base 16 to ensure string is valid hexadecimal digit.
    try:
        int(s_clean, 16) 
        return True
    except ValueError:
        return False
    
def parse_key(key_str: str) -> bytes:

    """Convert a key string into bytes.

    Accepts hex-encoded input (optional ``0x`` prefix and spaces) or a
    plain string, which is UTF-8 encoded.

    Raises:
        ValueError: If the key is empty or invalid.
    """

    # Converts string to bytes

    ks = key_str.strip()
    if is_hex_like(ks):
        ks = ks.lower()
        if ks.startswith("0x"):
            ks = ks[2:]
        ks = ks.replace(" ", "")
        if len(ks) == 0 or len(ks) % 2 != 0: # Must be even so try to devide by 2, if not possible send error.
            raise ValueError("Invalid key.") 
        try:
            return bytes.fromhex(ks) # Convert hex string to bytes
        except ValueError as e:
            raise ValueError(f"Invalid key: {e}")
    else:
        b = ks.encode("utf-8") # Convert plain string to bytes
        if not b:
            raise ValueError("Key is not allowed to be empty.")
        return b
    
def xor_bytes(data: bytes, key: bytes) -> bytes:

    """ XOR data with a repeating key. Returns b"" if data is empty. Raises ValueError if key is empty. """

    # Perform XOR operation between data and key.
    # The key is repeated (reused) if shorter than the data.

    if not data:
        return b""
    if not key:
        raise ValueError("Key is not allowed to be empty.")
    out = bytearray(len(data))
    klen = len(key)
    for i, b in enumerate(data):
        out[i] = b ^ key[i % klen] # XOR each byte with corresponding key byte
    return bytes(out)

def format_python_array(encrypted: bytes) -> str:
    
    """ Format bytes as a Python hex array string. """
    # Format bytes as a Python hex array string.

    hex_items = ", ".join(f"0x{b:02X}" for b in encrypted)
    return f"bytes([{hex_items}])\n"

def format_c_array(encrypted: bytes, var_name: str = "buf") -> str:
    
    """ Format bytes as a C hex array string. """
    # Format bytes as a C hex array string.

    hex_items = ", ".join(f"0x{b:02X}" for b in encrypted)
    return (
        f"unsigned char {var_name}[] = {{ {hex_items} }};\n"
        f"// length: {len(encrypted)}\n"
    )

def main() -> int:

    """
    Process input, XOR it with a key, and write the output in the chosen format.
    """
    
    args = parse_args()

    # Reads the imput as raw bytes.
    try:
        with open(args.inputfile, "rb") as f:
            data = f.read()
    except OSError as e:
        print(f"Not able to read input: {e}", file=sys.stderr)
        return 1

    if not data:
        print("Input is empty.", file=sys.stderr)
        return 1

    # Inserts the Key into input
    try:
        key = parse_key(args.key)
    except ValueError as e:
        print(f"Fel: {e}", file=sys.stderr)
        return 1

    # XOR the data with the key

    encrypted = xor_bytes(data, key)

    # Output depending on format

    if args.format == "raw":
        try:
            with open(args.outfile, "wb") as f:
                f.write(encrypted)
        except OSError as e:
            print(f"Wasnt able to write output: {e}", file=sys.stderr)
            return 1
    elif args.format == "python":
        content = format_python_array(encrypted)
        try:
            with open(args.outfile, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as e:
            print(f"Wasnt able to write output: {e}", file=sys.stderr)
            return 1
    elif args.format == "c":
        content = format_c_array(encrypted, var_name="buf")
        try:
            with open(args.outfile, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as e:
            print(f"Wasnt able to write output: {e}", file=sys.stderr)
            return 1
    else:
        print("Unknown Format.", file=sys.stderr)
        return 1
    
    # Print if success! 

    print(f"Done: Written {len(encrypted)} bytes to '{args.outfile}' with format '{args.format}'.")
    return 0

    
# Added so you can call on functions 

if __name__ == "__main__":
    raise SystemExit(main())

