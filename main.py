import tkinter as tk
from tkinter import messagebox, Text, StringVar, Entry, END, Toplevel, Label, Button
import base64
from PIL import Image, ImageTk

text2 = None  # Initialize text2 as a global variable

def encrypt():
    global text2  # Declare text2 as a global variable
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END).strip()  # Retrieve the message and remove trailing newline
        if message:
            screen1 = Toplevel(screen)
            screen1.title("Encryption")
            screen1.geometry("400x200")
            screen1.configure(bg="#ed3833")
            encode_message = message.encode("utf-8")  # Encode the message as bytes
            base64_bytes = base64.b64encode(encode_message)  # Encode using base64
            encrypt_msg = base64_bytes.decode("utf-8")  # Convert bytes to string
            Label(screen1, text="ENCRYPT", font="Arial", fg="white", bg="#ed3833").place(x=10, y=0)
            text2 = Text(screen1, font="Roboto 10", bg="white", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(tk.END, encrypt_msg)
        else:
            messagebox.showerror("Encryption Error", "Input text is empty.")
    elif password == "":
        messagebox.showerror("Encryption Error", "Input key")
    else:
        messagebox.showerror("Encryption Error", "Invalid key")

def reset():
    code.set("")
    text1.delete(1.0, END)
    if text2:
        text2.delete(1.0, END)  # Clear text2 if it exists

def decrypt():
    global text2  # Declare text2 as a global variable
    password = code.get()
    if password == "1234":
        encrypted_message = text2.get(1.0, END).strip()  # Retrieve the encrypted message
        if encrypted_message:
            try:
                # Decode the base64 encoded message
                decrypted_message = base64.b64decode(encrypted_message.encode('utf-8')).decode('utf-8')
                # Display the decrypted message
                text1.delete(1.0, END)
                text1.insert(END, decrypted_message)
            except base64.binascii.Error:
                messagebox.showerror("Decryption Error", "Invalid encrypted message.")
        else:
            messagebox.showerror("Decryption Error", "No encrypted message to decrypt.")
    elif password == "":
        messagebox.showerror("Decryption Error", "Input key")
    else:
        messagebox.showerror("Decryption Error", "Invalid key")

def main_screen():
    global screen
    screen = tk.Tk()
    screen.geometry("375x398")
    screen.title("Dialog box")

    # Load the image
    image = Image.open("keys.png")
    image = image.resize((50, 50))  # Resize the image as needed
    image_icon = ImageTk.PhotoImage(image)

    # Use a Label to display the image
    label_image = Label(screen, image=image_icon)
    label_image.image = image_icon  # Keep a reference to avoid garbage collection
    label_image.place(x=10, y=10)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=70, y=10)
    global text1
    text1 = Text(font="Roboto 12", bg="white", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
    text1.place(x=70, y=40, width=295, height=100)
    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=70, y=150)

    global code
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 20), show="*").place(x=70, y=180)
    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=70, y=220)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=245, y=220)
    Button(text="RESET", height="2", width=23, bg="#1089ff", fg="white", bd=0, command=reset).place(x=70, y=260)

    screen.mainloop()

main_screen()