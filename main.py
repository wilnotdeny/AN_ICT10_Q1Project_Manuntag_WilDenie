import tkinter as tk
from datetime import date

# colors
dark = "#4a0a12"
red = "#8b1423"
bright = "#c4283c"
white = "white"

products = ["Skate Deck", "Wheels Set", "Trucks Pair", "Bearings",
            "Grip Tape"]
prices = [1800, 950, 1500, 600, 250]

category_names = ["Decks", "Wheels", "Trucks", "Clothes", "Others"]
category_codes = ["DE", "WH", "TR", "CL", "OT"]

window = tk.Tk()
window.title("Skate Shop")
window.geometry("420x680")
window.config(bg=dark)


def show_receipt():
    sku_page.pack_forget()
    receipt_page.pack()


def show_sku():
    receipt_page.pack_forget()
    sku_page.pack()


top = tk.Frame(window, bg=red)
top.pack(fill="x")

tk.Button(top, text="Receipt Page", command=show_receipt).pack(
    side="left", padx=10, pady=10)
tk.Button(top, text="SKU Page", command=show_sku).pack(
    side="left", pady=10)


receipt_page = tk.Frame(window, bg=dark)

tk.Label(receipt_page, text="OBMC Entrep Fair", bg=dark, fg=white,
         font=("Arial", 20, "bold")).pack(pady=(15, 0))
tk.Label(receipt_page, text="Group 1 - Skate Shop", bg=dark,
         fg=white).pack(pady=(0, 15))

tk.Label(receipt_page, text="Customer Name", bg=dark, fg=white).pack()
name_box = tk.Entry(receipt_page, width=30)
name_box.pack(pady=5)

tk.Label(receipt_page, text="Products", bg=dark, fg=white,
         font=("Arial", 14, "bold")).pack(pady=(15, 5))

checks = []  
for i in range(len(products)):
    answer = tk.IntVar()
    text = products[i] + "  -  ₱" + str(prices[i])
    tk.Checkbutton(receipt_page, text=text, variable=answer, bg=dark,
                   fg=white, selectcolor=red, activebackground=dark,
                   activeforeground=white).pack(anchor="w", padx=80)
    checks.append(answer)


receipt_error = tk.Label(receipt_page, text="", bg=dark, fg="yellow")
receipt_error.pack(pady=5)


def make_receipt():
    customer = name_box.get()  
    total = 0  
    items = ""  
    count = 0 

 
    for i in range(len(products)):
        if checks[i].get() == 1:
            total = total + prices[i]
            count = count + 1
            items = items + products[i] + " - ₱" + str(prices[i]) + "\n"


    if customer == "":
        receipt_error.config(text="Please type your name.")
        return
    if count == 0:
        receipt_error.config(text="Please pick at least one item.")
        return


    receipt_error.config(text="")
    words = "Customer: " + customer + "\n"
    words = words + "Date: " + str(date.today()) + "\n"
    words = words + "-" * 30 + "\n"
    words = words + items
    words = words + "-" * 30 + "\n"
    words = words + "TOTAL: ₱" + str(total)
    receipt_label.config(text=words)


tk.Button(receipt_page, text="Create Order", bg=bright, fg=white,
          command=make_receipt).pack(pady=5)

receipt_label = tk.Label(receipt_page, text="Your order will appear here.",
                         bg=red, fg=white, font=("Courier", 10),
                         justify="left", width=38, pady=10)
receipt_label.pack(pady=10)


sku_page = tk.Frame(window, bg=dark)

tk.Label(sku_page, text="SKU Generator", bg=dark, fg=white,
         font=("Arial", 20, "bold")).pack(pady=(15, 15))


tk.Label(sku_page, text="Category", bg=dark, fg=white).pack()
category = tk.StringVar()
category.set(category_names[0])
tk.OptionMenu(sku_page, category, *category_names).pack(pady=5)

tk.Label(sku_page, text="Product Name", bg=dark, fg=white).pack(
    pady=(10, 0))
product_box = tk.Entry(sku_page, width=30)
product_box.pack(pady=5)


tk.Label(sku_page, text="Stock Quantity", bg=dark, fg=white).pack(
    pady=(10, 0))
stock_box = tk.Entry(sku_page, width=30)
stock_box.pack(pady=5)

sku_error = tk.Label(sku_page, text="", bg=dark, fg="yellow")
sku_error.pack(pady=5)


def make_sku():
    name = product_box.get().replace(" ", "")
    stock_text = stock_box.get()


    if len(name) < 3:
        sku_error.config(text="Product name needs at least 3 letters.")
        return
    if not stock_text.isdigit():
        sku_error.config(text="Stock must be a whole number.")
        return
    number = int(stock_text)
    if number > 999:
        sku_error.config(text="Stock must be 999 or less.")
        return

  
    sku_error.config(text="")
    part1 = category_codes[category_names.index(category.get())]  # 2 letters
    part2 = name[0:3].upper()  # first 3 letters of the name
    part3 = str(number).zfill(3)  # stock with zeros in front (3 digits)
    code = part1 + part2 + part3  # 2 + 3 + 3 = 8 characters
    sku_label.config(text=code)


tk.Button(sku_page, text="Generate SKU", bg=bright, fg=white,
          command=make_sku).pack(pady=5)

sku_label = tk.Label(sku_page, text="Your SKU will appear here.", bg=red,
                     fg=white, font=("Courier", 16, "bold"), width=26,
                     pady=20)
sku_label.pack(pady=20)


show_receipt()
window.mainloop()