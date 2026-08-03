import tkinter as tk
from tkinter import filedialog
import locale

def save():
    global root, text, btn
    stroka = text.get("1.0", tk.END)
    ptk = filedialog.asksaveasfilename(defaultextension=".txt")
    if ptk:  # Брандмауэр защиты от отмены окна Windows
        file = open(ptk, "w", encoding="utf-8")
        file.write(stroka); file.close()
        btn.config(text="Your file saved💾/Ваш файл сохраненен💾")

def deltext():
    global text
    text.delete("1.0", tk.END)

root = tk.Tk()
lng = locale.getdefaultlocale()[0]
root.title("Notepad++")
root.config(bg="black")

text = tk.Text(fg="green", bg="black", font=("Courier New", 11))
text.pack(pady=15, fill="both", expand=True)

btn = tk.Button(root, text="💾 Save/Сохранить", command=save, bg="green", fg="white", activebackground="darkgreen")
btn.pack(pady=10)

btndel = tk.Button(root, text="🗑️ Delete text/Удалить текст", command=deltext, bg="red", fg="white", activebackground="darkred")
btndel.pack(pady=15)

root.mainloop()
