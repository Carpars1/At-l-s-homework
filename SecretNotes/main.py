import tkinter as tk
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode('utf-8'))

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save_encrpty_notes():
    title_get = title_input.get()
    secret_get = secret_input.get("1.0", tk.END)
    masterkey_get = masterkey_label_input.get()

    if len(title_get) == 0 or len(secret_get) == 0 or len(masterkey_get) == 0 :
        messagebox.showinfo("Error", "Please Fill the Blanks")
    else:
        message_encrypted = encode(masterkey_get, secret_get)
        try:
            with open("Secret_note.txt", "a") as new_file:
                new_file.write(f"\n {title_get}\n{message_encrypted.decode('utf-8')}")
        except FileNotFoundError:
            with open("Secret_note.txt", "w") as new_file:
                new_file.write(f"\n {title_get}\n{message_encrypted.decode('utf-8')}")
        finally:
            title_input.delete(0, tk.END)
            masterkey_label_input.delete(0, tk.END)
            secret_input.delete("1.0", tk.END)

def decrpty_notes():
    try:
        with open("Secret_note.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                title = lines[i].strip()
                encrypted_message = lines[i + 1].strip()
                masterkey_get = masterkey_label_input.get()
                if masterkey_get:
                    decrypted_message = decode(masterkey_get, encrypted_message.encode('utf-8'))
                    messagebox.showinfo("Decrypted Message", f"Title: {title}\nMessage: {decrypted_message}")
                else:
                    messagebox.showinfo("Error", "Please enter the master key")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# UI
window = tk.Tk()
window.title("Secret Notes")
window.minsize(width=200, height=400)
window.config(padx=30, pady=30)

image = tk.PhotoImage(file="topsecret.png")
image_label = tk.Label(window, image=image)
image_label.pack()

title_label= tk.Label(text="Enter your Title")
title_label.pack()

title_input= tk.Entry(width=25)
title_input.pack()

secret_label = tk.Label(text="Enter your Secret")
secret_label.pack()

secret_input = tk.Text(width=30)
secret_input.pack()

masterkey_label = tk.Label(text="Enter your Masterkey ")
masterkey_label.pack()

masterkey_label_input=tk.Entry(width=25)
masterkey_label_input.pack()

save_encrpty_button = tk.Button(text="Save & Encrypt", command=save_encrpty_notes)
save_encrpty_button.pack()

decrpty_button = tk.Button(text="Decrypt", command=decrpty_notes)
decrpty_button.pack()

window.mainloop()