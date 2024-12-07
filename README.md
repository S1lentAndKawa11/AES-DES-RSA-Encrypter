# 📜 Text Encryption Tool  

A simple, user-friendly desktop application built with Python and Tkinter that provides **AES**, **DES**, and **RSA** encryption methods for securing text input.  

---

## 🚀 Features  
- **Encrypt Text:** Choose from AES, DES, or RSA encryption algorithms.  
- **Random Key Generation:** Keys are generated securely using cryptographic libraries.  
- **User-Friendly Interface:** Modern and interactive UI built with Tkinter.  
- **Cross-Platform Compatibility:** Works on Windows, macOS, and Linux.  

---

## 🛠️ Technologies Used  

- **Python 3.x** (Main Programming Language)  
- **Tkinter** (GUI Framework)  
- **pycryptodome** (AES, DES Encryption)  
- **rsa** (Public-Key Cryptography)  

---

## 📦 Installation  

### 1. Clone the Repository:

git clone

### 2. Create a virtual environment: 

python -m venv myvenv

### 3. Activate the virtual environment:

myvenv\Scripts\activate

### 4. Install dependencies:

pip install -r requirements.txt

### 5. Run the app:

python main.py



## 💻 Usage
**Launch the app.
Select an encryption algorithm (AES, DES, or RSA) from the dropdown menu.
Enter the text you want to encrypt in the input text box.
Click the Encrypt button to see the encrypted result in the output box.
Use the Clear button to reset the input and output fields.**




## 🧩 How It Works

## 🔐 AES & DES Encryption:
  Key Generation: Keys are generated using get_random_bytes().
  Padding: Text is padded for proper encryption.
  Encryption: The text is encrypted using the corresponding algorithm in CBC mode.
  Encoding: IV (Initialization Vector) and ciphertext are Base64-encoded for display.

## 🔒 RSA Encryption:
  Key Pair Generation: Public and private keys are generated dynamically using rsa.newkeys().
  Encryption: Text is encrypted using the public key.
  Encoding: Encrypted text is Base64-encoded for safe display.


## 📄 Requirements

  **pip          24.2
  pyasn1       0.6.1
  pycryptodome 3.21.0
  rsa          4.9**



**📜 License
This project is licensed under the MIT License. See the LICENSE file for details.**
