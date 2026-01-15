# 🔐 XOR File Encryption / Decryption Tool

A lightweight **Python XOR encryption and decryption utility** for files.  
Encrypt **any file**, output it in multiple formats, and decrypt it again using the **same key**.

> ⚠️ XOR is **symmetric** — encrypting twice with the same key restores the original data.

---

## ✨ Features

- Encrypts and decrypts **any file type**
- Supports **plaintext and hexadecimal keys**
- Automatically repeats the key if it is shorter than the input
- Multiple output formats for easy reuse
- Safe handling of binary files

---

## 📦 Supported Output Formats

| Format | Description |
|------|------------|
| `raw` | Writes encrypted bytes directly to a file |
| `python` | Outputs a Python `bytes([...])` array |
| `c` | Outputs a C `unsigned char` array with length |

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.7+
- No external dependencies

---

### ▶️ Running the Program

```bash
python inlamning.py
```

You will be prompted for:

- Input file path  
- Output file path  
- XOR key  
- Output format (`raw`, `python`, or `c`)

---

## 🔑 Key Formats

You can use **either plaintext or hexadecimal keys**.

### Plaintext Key Example

```text
mysecretkey
```

### Hexadecimal Key Examples

```text
0x41 42 43
```

```text
414243
```

---

## 🧠 How It Works

1. Reads the input file as raw bytes
2. Parses the key as plaintext or hexadecimal
3. XORs each byte of the file with the key (repeating as needed)
4. Writes the result using the selected output format

🔁 The same process is used for both encryption and decryption.

---

## 🧪 Example Workflow

Encrypt a file:

```text
input.bin → encrypted.bin
```

Decrypt the file:

```text
encrypted.bin → original.bin
```

✔️ Using the same key restores the original file.

---

## 🛑 Security Notice

> ⚠️ This tool is **not cryptographically secure**

XOR encryption is intended for:

- Educational purposes
- Learning file and byte manipulation
- Simple obfuscation
- Malware analysis and research

❌ Do **not** use this tool to protect sensitive or personal data.

---

## 📄 License

MIT License

---

## ⭐ Contributing

Pull requests, improvements, and suggestions are welcome.  
If you find this project useful, consider giving it a ⭐ on GitHub.
