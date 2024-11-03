from cProfile import label

import requests
import json
from  tkinter import  *
from tkinter import messagebox as mb

def exchange

#открываем окно
window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")
#делаем метку
label(text="Введите курс валюты").pack(padx=10, pady=10)
#добавим поле ввода
entry = Entry()
entry.pack(padx=10, pady=10)
#добавляем кнопку
Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)


window.mainloop()
