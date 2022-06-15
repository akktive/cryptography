import cryptography.fernet
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import messagebox as mb, filedialog


z = ""

# функция создания ключа шифрования
def write_key():
    global key
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)


# функция чтения ключа
def load_key():
    return open('crypto.key', 'rb').read()


# функция открытия и шифрования файла
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


# функция открытия и дешифрования файла
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)


# функция проверки существования ключа
def check_key():
    try:
        with open('crypto.key', 'rb'):
            global key
            key = load_key()
    except FileNotFoundError:
        write_key()
        key = load_key()


# фукнция изменения текста на кнопке при выборе файла
def dialog():
    foldername = filedialog.askopenfilename()
    if foldername:
        global z
        z = foldername
        foldername = "Выбран файл: " + foldername.split("/")[-1]
        name.config(text=foldername)


# фукнция вывода сообщения при шифровании
def encrypt_file():
    check_key()
    file = z
    try:
        with open(file, 'rb') as opened_file:
            encrypt(file, key)
        mb.showinfo("Успех", "Файл зашифрован!")
    except FileNotFoundError or FileExistsError:
        mb.showerror("Ошибка", "Файл не существует!")


# фукнция вывода сообщения при дешифровании
def decrypt_file():
    check_key()
    file = z
    try:
        with open(file, 'rb'):
            try:
                decrypt(file, key)
                mb.showinfo("Успех", "Дешифрование выполнено!")
            except cryptography.fernet.InvalidToken:
                mb.showerror("Ошибка", "Файл уже дешифрован!")
    except FileNotFoundError or FileExistsError:
        mb.showerror("Ошибка", "Файл не существует!")


# функция вывода информации о системе
def prog_info():
    mb.showinfo("Справка о системе", "Это программа позволяет\nшифровать и дешифровать любые\nфайлы на Вашем компьютере.")


win = Tk()
win.title("Cryptography")
win.geometry("320x220")
win.configure(bg="peachpuff")
name = Button(win, text="Выбрать файл", command=dialog)
name.place(relx=.5, rely=.4, anchor="center", width=200, height=30)
name.config(bg="#BE8C63", fg="white", font=("Courier", 9))

but = Button(win, text="Шифровать", command=encrypt_file)
but.place(relx=.3, rely=.69, anchor="center")
but.config(bg="#BE8C63", fg="white", font=("Courier", 10))

but2 = Button(win, text="Дешифровать", command=decrypt_file)
but2.place(relx=.7, rely=.69, anchor="center")
but2.config(bg="#BE8C63", fg="white", font=("Courier", 10))

but3 = Button(win, text="О системе", command=prog_info)
but3.place(relx=.85, rely=.1, anchor="center")
but3.config(bg="#BE8C63", fg="white", font=("Courier", 10))

win.mainloop()
