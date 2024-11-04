from cProfile import label

import requests
import json
from  tkinter import  *
from tkinter import messagebox as mb

from bottle import response


def exchange():
    code = entry.get()

    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                mb.showinfo("Курс обмена", f"Курс:{exchange_rate} {code} за один доллар")
            else:
                mb.showerror("Ошибка!",f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("ошибка",f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!","Введите код валюты!")

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
