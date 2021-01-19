from tkinter import *
import mysql.connector
from tkinter import messagebox
import datetime

mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                               host = "localhost", database = "lifechoicesonline",
                               auth_plugin = "mysql_native_password")

mycursor = mydb.cursor()

window = Tk()
window.title("Lifechoices Online")
window.geometry("450x450")
window.configure(background = "light green")

# WINDOW LABELS
headlb = Label(window, text = "LifeChoices Online", font=("bold", 20))
headlb.configure(background = "green")
headlb.place(x = 100, y = 10)

userlb = Label(window, text = "Username")
userlb.place(x = 100, y = 100)

passlb = Label(window, text = "Password")
passlb.place(x = 100, y = 150)

# ADMIN ENTRY
admin_ent = Entry(window)
admin_ent.place(x = 200, y = 100)

pass_ent = Entry(window, show = "*")
pass_ent.place(x = 200, y = 150)

def login():
    user_name = admin_ent.get()
    pass_word = pass_ent.get()
    sql = "select * from logins where username = %s and password = %s"
    mycursor.execute(sql, [(user_name), (pass_word)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def logged():
    window2 = Tk()
    window2.title("Cellphone Number")
    window2.geometry("300x100")
    window2.configure(background = "light green")

    mobilb = Label(window2, text = "Cellnumber")
    mobilb.place(x = 10, y = 10)
    mobi_ent = Entry(window2)
    mobi_ent.place(x = 100, y = 10)

    messagebox.showinfo("Login Successful", "Enjoy You Day")

def failed():
    messagebox.showerror("Login Unsuccessful","incorrect username or password.")

# LOGIN BUTTON
log_btn = Button(window,text = "Login", width = 5, command = login)
log_btn.place(x = 150, y = 200)

# REGISTER INTERFACE
def register():
    print("you hit return")

    window3 = Tk()
    window3.title("Register")
    window3.geometry("450x450")
    window3.configure(background = "light green")

    mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                                   host = "localhost", database = "lifechoicesonline",
                                   auth_plugin = "mysql_native_password")

    mycursor = mydb.cursor()

    # WINDOW3 LABELS
    full_lb = Label(window3, text = "Fullname")
    full_lb.place(x = 100, y = 50)
    user_name = Label(window3, text = "Username")
    user_name.place(x = 100, y = 100)
    user_pass = Label(window3, text = "Password")
    user_pass.place(x = 100, y = 150)

    # WINDOW3 ENTRIES
    full_ent = Entry(window3)
    full_ent.place(x = 200, y = 50)
    user_ent = Entry(window3)
    user_ent.place(x = 200, y = 100)
    pass_user = Entry(window3, show = "*")
    pass_user.place(x = 200, y = 150)

    # SIGN UP FUNCTION FOR INSERT BUTTON
    def sign_up():
        fname = full_ent.get()
        nameuser = user_ent.get()
        passname = pass_user.get()
        try:
            secsql = "insert into users(full_name,username,password) values(%s, %s, %s)"
            mycursor.execute(secsql,[(fname), (nameuser),(passname)])
            mydb.commit()
        except ValueError:
            print("Couldn't sign up")


    insert = Button(window3, text = "Sign up", command = sign_up, width = 25)
    insert.configure(background = "light blue")
    insert.place(x = 100, y = 200)

# ADMIN CHANGES
def key_press(event):
    print("event.char")

    admin_gui = Tk()
    admin_gui.title("Admin Login")
    admin_gui.geometry("450x450")
    admin_gui.bind("<Key>", key_press)

    # ADD BUTTON
    add_btn = Button(admin_gui, text = "Add Record")
    add_btn.place(x = 50, y = 200)

    # REMOVE BUTTON
    remove_data = Button(admin_gui, text = "Delete Record")
    remove_data.place(x = 150, y = 200)

    # GRANT PRIVILAGES BUTTON
    grant_btn = Button(admin_gui, text = "Grant Privilages")
    grant_btn.place(x = 250, y = 200)

sign_btn = Button(window, text = "Register" ,width = 5, command = register)
sign_btn.place(x = 250, y = 200)



window.mainloop()
