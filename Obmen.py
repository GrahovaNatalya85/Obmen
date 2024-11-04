import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

# Currency dictionary
cur = {
    "RUB": "Российский рубль",
    "EUR": "Евро",
    "GBP": "Британский фунт стерлингов",
    "JPY": "Японская йена",
    "CNY": "Китайский юань",
    "KZT": "Казахский тенге",
    "UZS": "Узбекский сум",
    "CHF": "Швейцарский франк",
    "AED": "Дирхам ОАЭ",
    "CAD": "Канадский доллар",
    "USD": "Американский доллар"
}

def update_b_label(event):
    b_code = b_combobox.get()
    b_name = cur.get(b_code, "Неизвестная валюта")  # Use b_code to get the name
    b_label.config(text=b_name)

def update_t_label(event):
    t_code = t_combobox.get()
    t_name = cur.get(t_code, "Неизвестная валюта")  # Use t_code to get the name
    t_label.config(text=t_name)

def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{b_code}")
            response.raise_for_status()
            data = response.json()
            if t_code in data["rates"]:
                exchange_rate = data["rates"][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}")
            else:
                mb.showerror("Ошибка!", f"Валюта {t_code} не найдена!")
        except requests.exceptions.RequestException as e:
            mb.showerror("Ошибка", f"Произошла ошибка при запросе: {e}.")
    else:
        mb.showwarning("Внимание!", "Выберите валюты!")

# Open the main window
window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x300")

# Base currency label and combobox
Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

# Target currency label and combobox
Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

# Button to get exchange rate
Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

# Start the Tkinter main loop
window.mainloop()