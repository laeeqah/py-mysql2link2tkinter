from tkinter import *
import mysql.connector
from tkinter import messagebox
from datetime import *
import os
import sys

mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                               host = "localhost", database = "lifechoicesonline",
                               auth_plugin = "mysql_native_password")

mycursor = mydb.cursor()


window = Tk()
window.title("Lifechoices Online")
window.geometry("450x450")
window.configure(background = "light green")

# DATETIME
now = datetime.now()
add_date = now.strftime("%d/%b/%Y")
today_date = now.strftime("%H:%M %p")
datetime = add_date+"\n"+today_date

lbd = Label(window, text = "", bg = "light green")
lbd['text'] = datetime
lbd.place(x = 180, y = 200)

# WINDOW LABELS
headlb = Label(window, text = "LifeChoices Online", font=("bold", 20))
headlb.configure(background = "green")
headlb.place(x = 100, y = 10)

userlb = Label(window, text = "Username")
userlb.place(x = 100, y = 100)

passlb = Label(window, text = "Password")
passlb.place(x = 100, y = 150)

pass_ent = Entry(window, show = "*")
pass_ent.place(x = 200, y = 150)

employ_ent = Entry(window)
employ_ent.place(x = 200, y = 100)



def login():
    user_name = employ_ent.get()
    pass_word = pass_ent.get()
    sql = "SELECT * FROM logins where username = %s and password = %s"
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

    # LOGIN BUTTON AND FUNCTION
    user_name = employ_ent.get()
    update_login = "UPDATE logins SET login_time = current_timestamp WHERE username=%s"
    mycursor.execute(update_login, [(user_name)])
    mydb.commit()

    mobilb = Label(window2, text = "Cellnumber")
    mobilb.place(x = 10, y = 10)
    mobi_ent = Entry(window2)
    mobi_ent.place(x = 100, y = 10)

    messagebox.showinfo("Login Successful", "Enjoy You Day")

    # LOGOUT BUTTON AND FUNCTION
    def logout():
        user_name = employ_ent.get()
        update_logout = "UPDATE logins SET logout_time = current_timestamp WHERE username = %s"
        mycursor.execute(update_logout[(user_name)])
        mydb.commit()
        window2.destroy()

    logout_btn = Button(window2, text = "Logout", command = logout)
    logout_btn.place(x = 20, y = 50)


def failed():
    messagebox.showerror("Login Unsuccessful","incorrect username or password.")

# LOGIN BUTTON
log_btn = Button(window,text = "Login", width = 10, command = login)
log_btn.place(x = 50, y = 250)


# REGISTER INTERFACE
def register():

    window3 = Tk()
    window3.title("Register")
    window3.geometry("450x450")
    window3.configure(background = "light green")

    mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                                   host = "localhost", database = "lifechoicesonline",
                                   auth_plugin = "mysql_native_password")

    mycursor = mydb.cursor()

    # WINDOW3 LABELS REGISTRATION
    full_lb = Label(window3, text = "Fullname")
    full_lb.place(x = 100, y = 50)
    user_name = Label(window3, text = "Username")
    user_name.place(x = 100, y = 100)
    user_pass = Label(window3, text = "Password")
    user_pass.place(x = 100, y = 150)

    # WINDOW3 ENTRIES REGISTRATION
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
           if full_ent.get() == "" or user_ent.get() == "" or passname == "":
                messagebox.showerror("Message", "Could not Register")
           else:
               secsql = "insert into users(full_name,username,password) values(%s, %s, %s)"
               mycursor.execute(secsql,[(fname), (nameuser),(passname)])
               mydb.commit()
               messagebox.showinfo("successful", "You Register")



        except Exception:
            messagebox.showerror("Message", "Could not Register")



    insert = Button(window3, text = "Sign up", command = sign_up, width = 25)
    insert.configure(background = "light blue")
    insert.place(x = 100, y = 250)

    # EXIT FUNCTION AND BUTTON
    def quit(): #Will make the function go back to the main screen
        window3.destroy()

    exit_btn = Button(window3, text = "Quit", command = quit, width = 25)
    exit_btn.configure(background = "red")
    exit_btn.place(x = 100,y = 300)

# ADMIN GUI
keyspressed = 0
def admin():

    mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                               host = "localhost", database = "lifechoicesonline",
                               auth_plugin = "mysql_native_password")

    mycursor = mydb.cursor()


    window.withdraw()
    global keyspressed
    admin_gui = Tk()
    admin_gui.title("Admin Login")
    admin_gui.geometry("750x550")
    admin_gui.configure(background = "light green")

    # ADMIN LABEL
    adlb = Label(admin_gui, text = "Welcome Admin", font = ("bold", 20))
    adlb.place(x = 200, y = 10)
    adlb.configure(background = "green")
    full_lb = Label(admin_gui, text = "Fullname")
    full_lb.place(x = 150, y = 100)
    user_name = Label(admin_gui, text = "Username")
    user_name.place(x = 150, y = 150)
    user_pass = Label(admin_gui, text = "Password")
    user_pass.place(x = 150, y = 200)

    # ADMIN_GUI ENTRIES REGISTRATION
    full_ent = Entry(admin_gui)
    full_ent.place(x = 250, y = 100)
    user_ent = Entry(admin_gui)
    user_ent.place(x = 250, y = 150)
    pass_user = Entry(admin_gui, show = "*")
    pass_user.place(x = 250, y = 200)

    # LOGIN LABEL
    loginlb = Label(admin_gui, text = "")
    loginlb.place(x = 10, y = 10)

    def add():
        login_ent = full_ent.get()
        nameuser = user_ent.get()
        passname = pass_user.get()


        entry = [full_ent.get(), user_ent.get(),pass_ent.get()]
        try:
            if entry == "":
                messagebox.showerror("Error", "Failed To Add The User")
            else:
                insert4logins = "insert into logins(full_name, username,password) values(%s, %s, %s)"
                mycursor.execute(insert4logins,[(login_ent), (nameuser),(passname)])
                mydb.commit()
                messagebox.showinfo("Message", "Successfully Added The User")

        except Exception:
            print("Couldn't add user")
        finally:
            print("The data might've gone through or not")


    # ADD BUTTON
    add_btn = Button(admin_gui, text = "Add Record", command = add)
    add_btn.place(x = 50, y = 300)

    def remove():
        nameuser = user_ent.get()
        delete = "delete from logins where username = %s"
        delete_reg = "delete from users where username = %s"
        mycursor.execute(delete,[(nameuser)])
        mycursor.execute(delete_reg,[(nameuser)])
        mydb.commit()
        user_ent.delete(0,END)
        full_ent.delete(0,END)
        pass_ent.delete(0,END)

    # REMOVE BUTTON
    remove_data = Button(admin_gui, text = "Delete Record",command = remove)
    remove_data.place(x = 200, y = 300)

    def check():

        secsql = mycursor.execute("select full_name,username,password,login_time, logout_time from logins ")
        loginlb['text'] += "People logged in:\n"
        loginlb['text'] += "fullname, username, password, login date(year, month, day) time(H:M:S)\n"
        for i in mycursor:
            logdata = str(i)
            #logdata = re.sub(',',':',logdata)
            logdata = re.sub('datetime.datetime','',logdata)
            logdata = logdata[1:-1]
            data = logdata.split('(')
            count =1
            for j in data:
                if count ==1:
                    loginlb['text']+=j[:-1]
                    count+=1
                elif count ==2:
                    loginlb['text']+=" <Login:> "+j[:-3]
                    count+=1
                elif count==3:
                    loginlb['text']+=" <Logout:> "+j[:-1]+"\n"
                    count+=1

            loginlb.place(x = 10, y = 400)

    # Check Button
    check_data = Button(admin_gui, text = "Check Record", command = check)
    check_data.place(x = 370, y = 300)

    def back():
        py = sys.executable
        os.execl(py,py, * sys.argv)



    back_btn = Button(admin_gui, text = "Back", command = back)
    back_btn.place(x = 400, y = 350)



# Control key
window.bind("<Control-a>", lambda x: admin())
label = Label(window)
label.place(x=0,y=0)

# REGISTER BUTTON CONNECT TO def register
sign_btn = Button(window, text = "Register" ,width = 10, command = register)
sign_btn.place(x = 300, y = 250)



window.mainloop()
