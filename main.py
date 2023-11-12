from tkinter import *
import requests

# color
main_color = "#007FFF"

# window
screen = Tk()
screen.title("Currency exchange")
screen.minsize(width=400, height=120)
screen.resizable(False, False)
screen.config(bg=main_color)
screen.iconbitmap("icon.ico")


# function
def count():
    try:
        currency_from = my_currency.get()
        currency_to = exchange_currency.get()
        amount = int(user_input.get())

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "Cesaj6Vu2SPHyXv9RljraeWvDB2TuIcR"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        response.raise_for_status()
        data_result = response.json()

        result_label.config(text = round(data_result["result"], 3))
        rate_label.config(text = f'Rate: {round(data_result["info"]["rate"], 3)}')
        notification_label.config(text="")
    except:
        notification_label.config(text = "Enter the amount.")

# user input
user_input = Entry(width=20, font=("Arial", 12), justify=CENTER)
user_input.insert(0, "0")  # default
user_input.grid(row=0, column=0, padx=10, pady=(10, 0))

# scroll bars
my_currency = StringVar(screen)
my_currency.set("CZK")  # default
my_currency_options = OptionMenu(screen, my_currency, "CZK", "EUR", "USD")
my_currency_options.grid(row=0, column=1, padx=10, pady=(10, 0))

exchange_currency = StringVar(screen)
exchange_currency.set("EUR")  # default
exchange_currency_options = OptionMenu(screen, exchange_currency, "CZK", "EUR", "USD")
exchange_currency_options.grid(row=1, column=1, padx=10, pady=(10, 0))

# button
count_button = Button(text="Count", font=("Arial", 12), command = count)
count_button.grid(row=0, column=2, padx=10, pady=(10, 0))

# result label
result_label = Label(text="0", bg=main_color, fg="white", font=("Arial", 12))
result_label.grid(row=1, column=0, padx=10, pady=(10, 0))

# rate label
rate_label = Label(bg=main_color, fg="white", font=("Arial", 12))
rate_label.grid(row=1, column=2, padx=10, pady=(10, 0))

# notification label
notification_label = Label(bg=main_color, fg="white", font=("Arial", 12))
notification_label.grid(row=2, column=0)


# main cycle
screen.mainloop()
