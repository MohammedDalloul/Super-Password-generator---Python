from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

GREEN = "#9FE2BF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for n in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for n in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    final_password = "".join(password_list)
    password_l.insert(0, final_password)
    pyperclip.copy(final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website_data = website_l.get()
    username_data = username_l.get()
    password_data = password_l.get()
    jsoned_data = {
        website_data : {
            "j_username": username_data,
            "j_password": password_data
        }
    }

    if len(website_data) != 0 and len(username_data) != 0 and len(password_data) != 0:

        try:
            with open("data.json", "r") as data:
                j_data = json.load(data)
                j_data.update(jsoned_data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(jsoned_data, data, indent=4)
        except json.JSONDecodeError:
            with open("data.json", "w") as data:
                json.dump(jsoned_data, data, indent=4)
        with open("data.json", "r") as data:
            j_data = json.load(data)
            j_data.update(jsoned_data)
            with open("data.json", "w") as data:
                json.dump(j_data, data, indent=4)

                website_l.delete(0, END)
                password_l.delete(0, END)
    else:
        messagebox.showerror(title="Oooops", message="Please make sure you fill all the required fields.")

# ---------------------------- FIND PASSWORD ------------------------------- #


def searching():
    website_data = website_l.get()
    try:
        with open("data.json", "r") as data:
            searching_data = json.load(data)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="You do not have a file of users and passwds!")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Your file is empty.")
    else:
        try:
            s_web = searching_data[website_data]
        except json.JSONDecodeError:
            messagebox.showerror(title="Error", message="Your file is empty.")
        except KeyError:
            messagebox.showerror(title="Error", message="Make sure you enter the website correctly!, it cannot be left "
                                                        "empty.")
        else:
            s_email = s_web["j_username"]
            s_password = s_web["j_password"]
            messagebox.showerror(title=f"{website_data}", message=f" email : {s_email}\npassword : {s_password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg=GREEN)

canvas = Canvas(height=200, width=200, highlightthickness=0, bg=GREEN)
lockpic = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lockpic)
canvas.grid(row=0, column=1)

website = Label(text="Website : ", bg=GREEN)
website.grid(row=1, column=0)

website_l = Entry(width=33)
website_l.grid(row=1, column=1)
website_l.focus()

search_button = Button(text="search", width=15, highlightthickness=0, command=searching)
search_button.grid(row=1, column=2)

username = Label(text="Username/Email : ", bg=GREEN)
username.grid(row=2, column=0)

username_l = Entry(width=52)
username_l.grid(row=2, column=1, columnspan=2)

password = Label(text="Password : ", bg=GREEN)
password.grid(row=3, column=0)

password_l = Entry(width=33)
password_l.grid(row=3, column=1)

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()



