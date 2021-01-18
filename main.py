from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                               host = "localhost", database = "lifechoicesonline",
                               auth_plugin = "mysql_native_password")

mycursor = mydb.cursor()

window = Tk()
window.title("Lifchoices Online")
window.geometry("450x450")
window.configure(background = "black")

# This is the labels
headlb = Label(window, text = "LifeChoices Online", font=("bold", 20))
headlb.configure(background = "green")
headlb.place(x = 100, y = 10)

userlb = Label(window, text = "Username")
userlb.place(x = 100, y = 100)

passlb = Label(window, text = "Password")
passlb.place(x = 100, y = 150)


# This is Entries
user_ent = Entry(window)
user_ent.place(x = 200, y = 100)

pass_ent = Entry(window)
pass_ent.place(x = 200, y = 150)

def login():
    user_name = user_ent.get()
    pass_word = pass_ent.get()
    sql = "select * from logins where username = %s and password = %s"
    mycursor.execute(sql, [(user_name), (pass_word)])
    results = mycursor.fetchall()
    if results:
        window.withdraw()
        for i in results:
            logged()
            break
    else:
        failed()

def logged():
    messagebox.showinfo("Login Successful", "Enjoy You Day")
    window2 = Tk()
    window2.title("Logged in")
    window2.geometry("450x450")

def failed():
    messagebox.showerror("Login Unsuccessful")

# Buttons
log_btn = Button(window,text = "Login", width = 5, command = login)
log_btn.place(x = 150, y = 200)

def register():
    print("you hit return")
    window3 = Tk()
    window3.title("Register")
    window3.geometry("450x450")
    mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                                   host = "localhost", database = "lifechoicesonline",
                                   auth_plugin = "mysql_native_password")

    mycursor = mydb.cursor()
    # Window3 labels
    full_lb = Label(window3, text = "Fullname")
    full_lb.place(x = 150, y = 50)

    # sql = "insert into users values()"
    # mycursor.execute(sql)


sign_btn = Button(window, text = "Register" ,width = 5, command = register)
sign_btn.place(x = 250, y = 200)



window.mainloop()
