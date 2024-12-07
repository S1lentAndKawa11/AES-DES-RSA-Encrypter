import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
import rsa
import base64

# AES Encryption
def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return {'iv': iv, 'ciphertext': ct}

# DES Encryption
def des_encrypt(text, key):
    cipher = DES.new(key, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode(), DES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return {'iv': iv, 'ciphertext': ct}

# RSA Encryption
def rsa_encrypt(text, public_key):
    return rsa.encrypt(text.encode(), public_key)

# Padding for AES and DES
def pad(text, block_size):
    pad_len = block_size - len(text) % block_size
    return text + bytes([pad_len] * pad_len)

# Function to handle encryption
def encrypt_text():
    choice = algo_choice.get()
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Input Error", "Please enter some text to encrypt.")
        return

    if choice == "AES":
        key = get_random_bytes(16)  # AES-128 key (16 bytes)
        encrypted = aes_encrypt(text, key)
    elif choice == "DES":
        key = get_random_bytes(8)  # DES key (8 bytes)
        encrypted = des_encrypt(text, key)
    elif choice == "RSA":
        (public_key, private_key) = rsa.newkeys(512)  # 512-bit RSA keys
        encrypted = rsa_encrypt(text, public_key)
        encrypted = base64.b64encode(encrypted).decode('utf-8')  # Base64 to ensure proper text encoding
    else:
        messagebox.showerror("Error", "Invalid algorithm choice.")
        return

    # Display the encrypted text
    if isinstance(encrypted, dict):
        encrypted_text.delete("1.0", tk.END)
        encrypted_text.insert(tk.END, f"IV: {encrypted['iv']}\nCiphertext: {encrypted['ciphertext']}")
    else:
        encrypted_text.delete("1.0", tk.END)
        encrypted_text.insert(tk.END, encrypted)

# Function to clear the input and output fields
def clear_fields():
    input_text.delete("1.0", tk.END)
    encrypted_text.delete("1.0", tk.END)

# Setup Tkinter window
root = tk.Tk()
root.title("Text Encryption")
root.geometry("600x500")
root.config(bg="#2c3e50")  # Blue background

# Header Label
header_label = tk.Label(root, text="Text Encryption Tool", font=("Helvetica", 18), pady=20, fg="white", bg="#2c3e50")
header_label.pack()

# Dropdown for algorithm choice
algo_choice = tk.StringVar(root)
algo_choice.set("AES")  # Default value

algo_menu = tk.OptionMenu(root, algo_choice, "AES", "DES", "RSA")
algo_menu.config(font=("Helvetica", 12), width=20, relief="solid", bg="#3498db", fg="white")
algo_menu.pack(pady=10)

# Input Textbox
input_text_label = tk.Label(root, text="Enter Text:", font=("Helvetica", 12), fg="white", bg="#2c3e50")
input_text_label.pack()

input_text = tk.Text(root, height=5, width=50, font=("Helvetica", 12), wrap=tk.WORD, bd=2, relief="sunken")
input_text.pack(pady=10)

# Encrypt Button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="raised")
encrypt_button.pack(pady=10)

# Clear Button
clear_button = tk.Button(root, text="Clear", command=clear_fields, font=("Helvetica", 12), bg="#e74c3c", fg="white", relief="raised")
clear_button.pack(pady=10)

# Encrypted Textbox
encrypted_text_label = tk.Label(root, text="Encrypted Text:", font=("Helvetica", 12), fg="white", bg="#2c3e50")
encrypted_text_label.pack()

encrypted_text = tk.Text(root, height=5, width=50, font=("Helvetica", 12), wrap=tk.WORD, bd=2, relief="sunken")
encrypted_text.pack(pady=10)

# Start Tkinter event loop
root.mainloop()
