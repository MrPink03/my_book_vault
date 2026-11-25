from tkinter import *
from tkinter import ttk


def add_book():
    book_name = name_entry.get()
    author_name = author_entry.get()
    book_category = category_combo.get()
    price = prices_spinbox.get()

    with open("books.txt", "a") as file:
        file.write(
            f"Book Name: {book_name}\n"
            f"Author: {author_name}\n"
            f"Category: {book_category}\n"
            f"Price(LKR): {price}\n\n"
        )


window = Tk()
window.title("Book Vault")
window.geometry("500x500")

name_label = Label(window, text="Name")
name_label.pack()

name_entry = Entry(window)
name_entry.pack()

author_label = Label(window, text="Author")
author_label.pack()

author_entry = Entry(window)
author_entry.pack()

category_label = Label(window, text="Category")
category_label.pack()

category_combo = ttk.Combobox(
    window,
    values=["novels", "science fictions"],
    state="readonly"
)
category_combo.pack()

prices_label = Label(window, text="Price(Rs.)")
prices_label.pack()

prices_spinbox = Spinbox(window, from_=500, to=1000, increment=100)
prices_spinbox.pack()

add_btn = Button(window, text="Add", command=add_book)
add_btn.pack(pady=10)

window.mainloop()