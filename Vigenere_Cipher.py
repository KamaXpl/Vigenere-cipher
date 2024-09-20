import tkinter as tk
from tkinter import messagebox

def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_length = len(key)
    
    for i, letter in enumerate(plaintext):
        if letter.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            base = ord('A') if letter.isupper() else ord('a')
            result.append(chr((ord(letter) - base + shift) % 26 + base))
        else:
            result.append(letter)
    
    return ''.join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_length = len(key)
    
    for i, letter in enumerate(ciphertext):
        if letter.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            base = ord('A') if letter.isupper() else ord('a')
            result.append(chr((ord(letter) - base - shift) % 26 + base))
        else:
            result.append(letter)
    
    return ''.join(result)

def encrypt():
    plaintext = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    
    if not plaintext or not key:
        messagebox.showwarning("Input Error", "Both the plaintext and key must be provided.")
        return
    
    encrypted_text = vigenere_encrypt(plaintext, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

def decrypt():
    ciphertext = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    
    if not ciphertext or not key:
        messagebox.showwarning("Input Error", "Both the ciphertext and key must be provided.")
        return
    
    decrypted_text = vigenere_decrypt(ciphertext, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

root = tk.Tk()
root.title("Vigenère Cipher")

# Labels, Entry
tk.Label(root, text="Input Text:").pack()
input_text = tk.Text(root, width=20, height=5)
input_text.pack()

tk.Label(root, text="Key: ").pack()
key_entry = tk.Entry(root)
key_entry.pack()

tk.Label(root, text="Output Text:").pack()
output_text = tk.Text(root, width=20, height=5)
output_text.pack()

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack()
root.mainloop()
