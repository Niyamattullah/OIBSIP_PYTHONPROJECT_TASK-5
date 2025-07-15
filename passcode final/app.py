import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for length.")
        return

    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    exclude_chars = exclude_entry.get()

    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    # Exclude characters
    chars = ''.join([c for c in chars if c not in exclude_chars])

    if not chars:
        result_var.set("Please select character types.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_var.set(password)

# Function to copy password
def copy_password():
    pyperclip.copy(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# --- GUI Setup ---
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("450x400")
root.configure(bg="#1c1b29")

# --- Styles ---
label_style = {"bg": "#1c1b29", "fg": "#e0d6f5", "font": ("Segoe UI", 10)}
entry_style = {"bg": "#3a345c", "fg": "#ffffff", "insertbackground": "#ffffff", "font": ("Segoe UI", 10), "relief": tk.FLAT}
check_style = {"bg": "#1c1b29", "fg": "#e0d6f5", "selectcolor": "#3a345c", "activebackground": "#1c1b29", "font": ("Segoe UI", 10)}

# --- Widgets ---
tk.Label(root, text="Random Password Generator", bg="#1c1b29", fg="#e4c2ff", font=("Segoe UI", 14, "bold")).pack(pady=10)

tk.Label(root, text="Password Length:", **label_style).pack(anchor="w", padx=30)
length_entry = tk.Entry(root, **entry_style)
length_entry.insert(0, "12")
length_entry.pack(fill="x", padx=30, pady=5)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var, **check_style).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, **check_style).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, **check_style).pack(anchor="w", padx=30)

tk.Label(root, text="Exclude Characters:", **label_style).pack(anchor="w", padx=30, pady=(10, 0))
exclude_entry = tk.Entry(root, **entry_style)
exclude_entry.pack(fill="x", padx=30, pady=5)

tk.Button(root, text="Generate Password", command=generate_password,
          bg="#824fff", fg="white", font=("Segoe UI", 10, "bold"), relief=tk.FLAT).pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, wraplength=400, bg="#3a345c", fg="#ffffff",
                        font=("Segoe UI", 10), height=2, width=40, relief=tk.FLAT)
result_label.pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_password,
          bg="#2e2a44", fg="#ffffff", font=("Segoe UI", 10), relief=tk.FLAT).pack()

root.mainloop()
