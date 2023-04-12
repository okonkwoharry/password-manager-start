from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_number + password_symbol

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_written = website_entry.get().lower()
    email_written = email_entry.get().lower()
    password_written = password_entry.get()
    new_data = {
        website_written: {
            "email": email_written,
            "password": password_written
        }
    }

    if len(website_written) == 0 or len(email_written) == 0 or len(password_written) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                #Reading old data
                data = json.load(file)
                #Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")



def find_password():
    website_written = website_entry.get().lower()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website_written in data:
                email_variable = data[website_written]["email"]
                password_variable = data[website_written]["password"]
                messagebox.showinfo(title="Details", message=f"Your {website_written} info is \n Email: {email_variable} \n Password: {password_variable}")
            else:
                messagebox.showinfo(title="Details", message="No details for the website exists")

    except FileNotFoundError:
        messagebox.showinfo(title="Details", message="No Data File Found")







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize()
window.config(pady=50, padx=50)

my_pass_canvas = Canvas(width=200, height=200)
my_pass_img = PhotoImage(file="logo.png")
my_pass_canvas.create_image(100, 100, image=my_pass_img)
my_pass_canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 12, "normal"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("Arial", 12, "normal"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Arial", 12, "normal"))
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "okonkwo.me1000@gmail.com")


password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", font=("Arial", 11, "normal"), width=13, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", font=("Arial", 12, "normal"), width=13, command=find_password)
search_button.grid(row=1, column=2)



window.mainloop()